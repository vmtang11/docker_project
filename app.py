#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Hello World! Welcome to my docker project')

if __name__ == '__main__':
    hello()