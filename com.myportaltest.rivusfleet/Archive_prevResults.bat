@echo off
title Archive Last Execution Results
set currMM=%date:~3,2%
set currYY=%date:~6,4%
set currDD=%date:~0,2%
set currMin=%time:~3,2%
set currSec=%time:~6,5%
set currHr=%time:~0,2%
zip -r Results\ArchivedResults\Screenshot_%currDD%.%currMM%.%currYY%.%currHr%.%currMin%.%currSec%.zip Results\ScreenShots
cd ./Results/ScreenShots
del *.png && cd ..
echo ScreenShot archive Successfull
echo %cd%
zip -r ArchivedResults\Reports_%currDD%.%currMM%.%currYY%.%currHr%.%currMin%.%currSec%.zip Reports
echo %cd%
rmdir /s /q Reports && mkdir Reports
echo Reports archive Successfull
pause