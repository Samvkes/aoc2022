#!/bin/bash
cookie="session=eenlangestringlettersencijfers"
dag=$1
naam="dag${dag}"
mkdir ${naam}
cd ${naam}
touch ${naam}.py
curl --cookie ${cookie} "https://adventofcode.com/2022/day/${dag}/input" > input.txt
