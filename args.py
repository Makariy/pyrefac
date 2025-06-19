from argparse import Action, ArgumentParser
from config import (
    RefactorConfig,
    RefactorAction,
    RenameModuleConfig,
    MoveSymbolConfig,
)


EXCLUDED_FILES = [
    "*.pyc",
    "*~",
    ".ropeproject",
    ".hg",
    ".svn",
    "_svn",
    ".git",
    ".tox",
    ".venv",
    "venv",
    ".mypy_cache",
    ".pytest_cache"
]

def _try_add_autocomplete(parser: ArgumentParser, file_args: list[Action]) -> None:
    try:
        from argcomplete import autocomplete, completers
    except ImportError:
        return

    autocomplete(parser)
    for arg in file_args:
        setattr(arg, "completer", completers.FilesCompleter())


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="refac", description="Refactor Python code")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Dry run (does not apply changes, only prints them)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print changes that will be applied",
    )

    parser.add_argument(
        "-p", "--project-root", default=".", help="Sets the project root"
    )

    parser.add_argument(
        "-s", "--show-files", action="store_true", help="Show files that will change"
    )

    parser.add_argument(
        "-e", "--exclude", action="append", default=[], help="Excluded files/directories"
    )

    file_args: list[Action] = []
    subparsers = parser.add_subparsers(
        dest="action", required=True, help="Action to perform"
    )

    rename = subparsers.add_parser("rename-module", help="Rename a module.")
    file_args.append(rename.add_argument("source", help="Source path"))
    file_args.append(rename.add_argument("dest", help="New filename"))

    move_symbols = subparsers.add_parser(
        "move-symbol", help="Move a symbol to another file"
    )
    file_args.append(move_symbols.add_argument("source", help="Source path"))
    move_symbols.add_argument("symbol", help="Symbols to move")
    file_args.append(move_symbols.add_argument("dest", help="Destination path"))

    _try_add_autocomplete(parser, file_args)

    return parser


def parse_config(parser: ArgumentParser) -> RefactorConfig:
    args = parser.parse_args()
    args.exclude += EXCLUDED_FILES
    action = RefactorAction(args.action)
    if action == RefactorAction.RENAME_MODULE:
        config = RenameModuleConfig(
            source=args.source,
            dest=args.dest,
        )
    elif action == RefactorAction.MOVE_SYMBOL:
        config = MoveSymbolConfig(
            source=args.source,
            symbol=args.symbol,
            dest=args.dest,
        )
    else:
        raise ValueError(f"Unsupported action: {action}")

    return RefactorConfig(
        action=action,
        config=config,
        is_dry_run=args.dry_run,
        is_verbose=args.verbose,
        show_files=args.show_files,
        project_root=args.project_root,
        excluded_files=args.exclude
    )
