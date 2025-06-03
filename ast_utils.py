import ast 
from rope.base.pynamesdef import DefinedName
from rope.base.pyobjectsdef import PyClass, PyFunction, PyModule
from file_utils import get_module_string_content


def _get_func_offset_from_ast_node(source: str, node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    lines = source.splitlines(keepends=True)
    line_offset = sum(len(line) for line in lines[:node.lineno - 1])
    base_offset = line_offset + node.col_offset 
    if isinstance(node, ast.FunctionDef):
        return base_offset + len("def ")
    else:
        return base_offset + len("async def ")


def _get_class_offset_from_ast_node(source: str, node: ast.ClassDef) -> int:
    lines = source.splitlines(keepends=True)
    line_offset = sum(len(line) for line in lines[:node.lineno - 1])
    base_offset = line_offset + node.col_offset 
    return base_offset + len("class ")


def get_offset_for_function(
    module: PyModule,
    func_name: str 
) -> int:
    func: DefinedName = module.get_attribute(func_name)
    obj: PyFunction = func.get_object()

    offset = _get_func_offset_from_ast_node(
        get_module_string_content(module),
        obj.get_ast()
    )
    return offset


def get_offset_for_class(
    module: PyModule,
    class_name: str 
) -> int:
    cls: DefinedName = module.get_attribute(class_name)
    obj: PyClass = cls.get_object()

    offset = _get_class_offset_from_ast_node(
        get_module_string_content(module),
        obj.get_ast()
    )
    return offset


