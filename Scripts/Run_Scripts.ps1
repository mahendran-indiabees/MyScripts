$SourceFilePath="C:\Users\Mahendran\Desktop\hostnames.txt"
$Failed_Hosts=""
$Success_Hosts=""
$FileContent=Get-Content  "$SourceFilePath"
foreach($hostvalue in $FileContent)
{
	echo "----------------# Host name : $hostvalue #----------------"
    ping $hostvalue -n 5 > null
    if($LASTEXITCODE -eq 0)
    {
        echo "Ping : $hostvalue is [SUCCESS]"
        echo "`n"
        $Hostval=$hostvalue+","
        $Success_Hosts+=$Hostval
    }
    else
    {
        echo "[Ping Failed] - Waiting for 10 seconds and retry the process ..."
	Start-Sleep -Seconds 10
        echo "`n"
        ping $hostvalue -n 5 > null
            if($LASTEXITCODE -eq 0)
            {
                echo "Ping : $hostvalue is [SUCCESS]"
                echo "`n"
                $Hostval=$hostvalue+","
                $Success_Hosts+=$Hostval
            }
            else
            {
                echo "Ping : $hostvalue is [FAILED]"
                echo "`n"
                $Host_val=$hostvalue+","
                $Failed_Hosts+=$Host_val
            }

    }
}
echo "`n"
echo "`n"
echo "********************************************"
echo "Successful hosts are [ $Success_Hosts ]"
echo "Failed Hosts are [ $Failed_Hosts ]"
echo "********************************************"


