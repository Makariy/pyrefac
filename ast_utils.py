import ast
from rope.base.pynamesdef import DefinedName
from rope.base.pyobjects import PyObject
from rope.base.pyobjectsdef import PyClass, PyFunction, PyModule
from file_utils import get_module_string_content


def _get_object_ast_by_symbol(module: ast.Module, symbol: str) -> ast.Name:
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == symbol:
                return target
            elif isinstance(target, (ast.Tuple, ast.List)):
                for elt in target.elts:
                    if not isinstance(elt, ast.Name) or elt.id != symbol:
                        continue
                    return elt

    raise ValueError(f"No object with id <{symbol}>")


def _get_base_offset_for_node(source: str, node: ast.stmt | ast.expr) -> int:
    lines = source.splitlines(keepends=True)
    line_offset = sum(len(line) for line in lines[: node.lineno - 1])
    return line_offset + node.col_offset


def _get_func_offset(source: str, node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    base_offset = _get_base_offset_for_node(source, node)
    if isinstance(node, ast.FunctionDef):
        return base_offset + len("def ")
    else:
        return base_offset + len("async def ")


def _get_class_offset(source: str, node: ast.ClassDef) -> int:
    base_offset = _get_base_offset_for_node(source, node)
    return base_offset + len("class ")


def _get_object_offset(source: str, module: ast.Module, symbol: str) -> int:
    node = _get_object_ast_by_symbol(module, symbol)
    return _get_base_offset_for_node(source, node)


PySymbol = PyFunction | PyClass | PyObject


def get_offset_for_symbol(module: PyModule, symbol: str) -> int:
    func: DefinedName = module.get_attribute(symbol)
    obj: PySymbol = func.get_object()

    if isinstance(obj, PyFunction):
        offset = _get_func_offset(get_module_string_content(module), obj.get_ast())
    elif isinstance(obj, PyClass):
        offset = _get_class_offset(get_module_string_content(module), obj.get_ast())
    elif isinstance(obj, PyObject):
        offset = _get_object_offset(
            get_module_string_content(module), module.get_ast(), symbol
        )
    else:
        raise ValueError("Unknown symbol type")

    return offset


def get_module_symbols(tree: ast.Module) -> set[str]:
    symbols: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    symbols.add(target.id)
                elif isinstance(target, (ast.Tuple, ast.List)):
                    for elt in target.elts:
                        if isinstance(elt, ast.Name):
                            symbols.add(elt.id)

        elif isinstance(node, ast.FunctionDef):
            symbols.add(node.name)

        elif isinstance(node, ast.ClassDef):
            symbols.add(node.name)

    return symbols

