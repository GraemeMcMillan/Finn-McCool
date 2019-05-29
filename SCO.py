#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 258 01:34:40 2019

@author: finnmccool
"""
import os

import pandas as pd
from pandas import ExcelWriter


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


def get_input_file():
    """Ask for the Input File name"""
    print('Is your xlsx file listed here?')
    T_files = os.listdir()
    my_files = [f for f in T_files if f.endswith('.' + 'xlsx')]
    for i in range(len(my_files)):
        print(i, ' ', my_files[i])
    checkfile = int(input('Enter number of the file to convert..> '))
    print('\nYou have chosen ', my_files[checkfile], '\n')
    return my_files[checkfile]


def get_df(file):
    """Create a Data Frame from the input file"""
    dframe = pd.read_excel(file)
    return dframe


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
        print('Team ', i, ' is ', x[i])

    while True:
        Team = str(input('Enter your team name ..> '))
        if Team in get_teams():
            return Team
        else:
            print('Yor Team is not in the list. Please retype!!')


def get_games(Team):
    """This ugly but the games are organised Home and Away"""
    temp = df[df.HomeTeam == Team]
    temp1 = df[df.AwayTeam == Team]
    TeamStats = pd.concat([temp, temp1])
    TeamStats = TeamStats.sort_values(by=['Date'])

    return TeamStats


def write_output_file(file):
    """Write the data out to the original file with the team name as a new sheet"""
    output_file = file[:-5]+Team + '.xlsx'
    teamstats_file = ExcelWriter(output_file)
    TeamStats.to_excel(teamstats_file, sheet_name=Team, index=False)
    teamstats_file.save()


def create_excel_file(file):
    """WIll create an excel file based on your team choice"""
    write_excel_file = input(
        'Do you want to write the out put to an Excel file? y(Y) or n(N)...>')
    if write_excel_file in {'Y', 'y'}:
        write_output_file(file)


"""Main Loop"""
start_prog_info()
input_file = get_input_file()
df = get_df(input_file)
Team = get_team_name()
TeamStats = get_games(Team)
create_excel_file(input_file)
