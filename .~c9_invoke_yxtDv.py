import click

@click.command()
@click.option('--pp', type = float)
@click.option('--hoa', type = float)
@click.option('--tax', type = float)
@click.option('--ins', type = float)
@click.option('--rent', type = float)
def cash_on_cash(pp, hoa, tax, ins, rent):
    '''
    Calculate cash on cash
    Inputs: pp - purchase price
            hoa - monthly hoa fee
            tax - monthly property tax
            ins - monthly home insurance
            rent - monthly rent
    Output: cash on cash in percent
    '''
    dep = 27.5
    yr_dep = pp/dep
    yr_tax = tax * 12
    yr_hoa = hoa * 12
    yr_ins = ins * 12
    expenses = yr_tax + yr_hoa + yr_ins
    
    yr_rent = rent * 12
    
    btcf = yr_rent - expenses
    cash_on_cash = btcf/pp * 100
    
    click.echo('Your estimated cash on cash is {0:.2f}%.'.format(cash_on_cash))
    
if __name__ == '__main__':
    cash_on_cash()