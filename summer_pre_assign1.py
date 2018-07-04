import click
import sys


@click.group()
@click.option('--removedigits/--no--removedigits', default=False)
@click.pass_context
def cli(ctx,removedigits):
    ctx.obj['removedigits']=removedigits


@cli.command()
@click.argument('list',nargs=-1)
@click.option('-d',default=None)
@click.pass_context
def concat(ctx,list,d):
    string = ''
    removedigits = ctx.obj['removedigits']
    l = list
    if(d==None):
        d=""


    if (removedigits):
        for indi in l:
            result = "".join(i for i in indi if not i.isdigit())
            string += result+d

    else:
        string=d.join(l)
    click.echo(string)


@cli.command()
@click.argument('list',nargs=-1)
@click.pass_context
def lower(ctx,list):
    removedigits = ctx.obj['removedigits']
    l = list
    if (removedigits):
        for indi in l:
            indi=indi.lower()
            result = "".join(i for i in indi if not i.isdigit() and i.lower())

        click.echo(result)
    else:
        for indi in l:
            indi=indi.lower()
            result = "".join(i.lower() for i in indi)
        click.echo(result)

@cli.command()
@click.argument('list',nargs=-1)
@click.pass_context
def upper(ctx,list):
    removedigits = ctx.obj['removedigits']
    l = list
    if (removedigits):
        for indi in l:
            indi=indi.upper()
            result = "".join(i for i in indi if not i.isdigit())

        click.echo(result)
    else:
        for indi in l:
            indi.upper()
            result = "".join(i.upper() for i in indi)
        click.echo(result)


if __name__=='__main__':
    cli(obj={})



