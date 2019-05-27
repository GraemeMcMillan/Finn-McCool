"""Use the SCO xlsx file to load a data frame into pandas
Courtesy of footbal-data.com"""

import os

import pandas as pd
from pandas import ExcelWriter

input_file = 'SCOFinal.xlsx'

# Create a data frame for the imput file
df = pd.read_excel(input_file)

# Define a variable for the column headings
Labels = [df.columns]


def start_prog_info():
    """Create some starting info"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print('****************************************************************************')
    print('* This only works for the excel file from Footbal-Data.co.uk Many Thanks!  *')
    print('* Give the team name and decide whether to output to an excel file or not. *')
    print('* The original file is a .csv file imported into excel (or Libre Calc)     *')
    print('* The excel file is called SCOFinal.xls                                    *')
    print('* A file called SCOFinal(team name).xlsx will be written. If you want!     *')
    print('****************************************************************************')
    print('\n\n')
    
def get_file():
    print('Is your file here?')
    print(os.listdir())
    checkfile = str(input('Enter file name to convert..> '))
    if os.path.exists(checkfile):
        print('File Name OK')
    else:
        print('File does not exisit')


def get_teams():
    """Create a set of team names removing duplicates"""
    teams = set()
    for i in range(len(df['HomeTeam'])):
        teams.add(df['HomeTeam'][i])
    return sorted(list(teams))


def get_team_name():
    """Enter your team name - match from list"""
    print('The list of teams is:  ')
    x = get_teams()
    for i in range(len(x)):
        print('Team ',i,' is ',x[i])

    while True:
        Team = str(input('Enter your team name ..> '))
        if Team in get_teams():
            return Team
        else:
            print('Yor Team is not in the list. Please retype!!')


def get_games(Team):
    """This ugly but the games are organised H and A"""
    temp = df[df.HomeTeam == Team]
    temp1 = df[df.AwayTeam == Team]
    TeamStats = pd.concat([temp, temp1])
    return TeamStats


def write_output_file():
    """Write the data out to the original file with the team name as a new sheet"""
    output_file = input_file[:-5]+Team + '.xlsx'
    writer = ExcelWriter(output_file)
    TeamStats.to_excel(writer, sheet_name=Team, index=False)
    writer.save()


def create_excel_file():
    """WIll create an excel file based on your team choice"""
    write_excel_file = input(
        'Do you want to write the out put to an Excel file? y(Y) or n(N)...>')
    if write_excel_file in {'Y', 'y'}:
        write_output_file()


"""This is the Main Programme"""
start_prog_info()
get_file()
Team = get_team_name()
TeamStats = get_games(Team)
create_excel_file()
