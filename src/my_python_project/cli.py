"""Command-line interface for My Python Project.

Provides commands for common operations and demonstrates Click best practices
with structured logging integration.
"""

import sys

import click

from my_python_project.core.config import settings
from my_python_project.utils.logging import get_logger

logger = get_logger(__name__)


@click.group()
@click.version_option(version="0.1.0", prog_name="my_python_project")
@click.option(
    "--debug",
    is_flag=True,
    help="Enable debug logging",
)
@click.pass_context
def cli(ctx: click.Context, debug: bool) -> None:
    """My Python Project - A short description of the project."""
    # Store debug flag in context for subcommands
    ctx.ensure_object(dict)
    ctx.obj["debug"] = debug

    if debug:
        logger.debug("Debug mode enabled")


@cli.command()
@click.option(
    "--name",
    "-n",
    type=str,
    default="World",
    help="Name to greet",
)
@click.pass_context
def hello(ctx: click.Context, name: str) -> None:
    """Greet the user with a personalized message."""
    try:
        debug = ctx.obj.get("debug", False) if ctx.obj else False

        logger.info(
            "Processing hello command",
            name=name,
            debug=debug,
        )

        message = f"Hello, {name}!"
        click.echo(message)

        logger.info("Command completed successfully", result=message)

    except Exception as e:
        logger.error("Command failed", error=str(e), exc_info=True)
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.pass_context
def config(ctx: click.Context) -> None:
    """Display current configuration settings.

    Shows configuration values from environment variables or defaults.
    """
    try:
        debug = ctx.obj.get("debug", False) if ctx.obj else False

        logger.info("Retrieving configuration")

        click.echo("Current Configuration:")
        click.echo("  Project: My Python Project")
        click.echo("  Version: 0.1.0")
        click.echo(f"  Debug: {debug}")
        click.echo(f"  Log Level: {settings.log_level}")

        logger.info("Configuration displayed successfully")

    except Exception as e:
        logger.error("Failed to display configuration", error=str(e), exc_info=True)
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    cli()
