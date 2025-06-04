from argparse import Action, ArgumentParser
from config import (
    RefactorConfig,
    RefactorAction,
    RenameModuleConfig,
    MoveClassConfig,
    MoveFuncConfig
)


def _try_add_autocomplete(
    parser: ArgumentParser,
    file_args: list[Action]
) -> None:
    try:
        from argcomplete import autocomplete, completers
    except:
        return 

    autocomplete(parser)
    for arg in file_args:
        arg.completer = completers.FilesCompleter()


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="refac",
        description="Refactor Python code"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Dry run (does not apply changes, only prints them)"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print changes that will be applied"
    )
    
    file_args: list[Action] = []
    subparsers = parser.add_subparsers(dest="action", required=True, help="Action to perform")

    rename = subparsers.add_parser("rename-module", help="Rename a module. Note: could be either file or directory")
    file_args.append(rename.add_argument("source", help="Source path"))
    file_args.append(rename.add_argument("dest", help="Destination path"))

    move_class = subparsers.add_parser("move-class", help="Move a class to another file")
    file_args.append(move_class.add_argument("source", help="Source filename"))
    move_class.add_argument("class_name", help="Class name to move")
    file_args.append(move_class.add_argument("dest", help="Destination filename"))

    move_func = subparsers.add_parser("move-func", help="Move a function to another file")
    file_args.append(move_func.add_argument("source", help="Source filename"))
    move_func.add_argument("func_name", help="Function name to move")
    file_args.append(move_func.add_argument("dest", help="Destination filename"))

    _try_add_autocomplete(parser, file_args)

    return parser


def parse_config(parser: ArgumentParser) -> RefactorConfig:
    args = parser.parse_args()
    action = RefactorAction(args.action)
    if action == RefactorAction.RENAME_MODULE:
        config = RenameModuleConfig(source=args.source, dest=args.dest)
    elif action == RefactorAction.MOVE_CLASS:
        config = MoveClassConfig(source=args.source, class_name=args.class_name, dest=args.dest)
    elif action == RefactorAction.MOVE_FUNC:
        config = MoveFuncConfig(source=args.source, func_name=args.func_name, dest=args.dest)
    else:
        raise ValueError(f"Unsupported action: {action}")

    return RefactorConfig(
        action=action,
        config=config,
        is_dry_run=args.dry_run,
        is_verbose=args.verbose 
    )

