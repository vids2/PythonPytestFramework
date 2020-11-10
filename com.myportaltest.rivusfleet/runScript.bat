@echo off
title Test Execution
pytest -vv -s --junitxml=.\Results\Reports\report.xml --html=.\Results\Reports\rep.html
pause