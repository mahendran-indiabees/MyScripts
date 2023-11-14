#----------------------- # Find  Old files and Archive it #----------------------- #

###  Get the Log Path from WinConnect Script [Log Path Extracted from CSV file]
$LogPath=$arg[0]

#variable declaration
$OldFilesPeriod="-30"
$RemoveLogPath=$LogPath
$excludeFiles="*.zip"


try 
{
  #Display existing files
  echo "Display Current files in Directory : [$RemoveLogPath]"
	if(($RemoveLogPath -ne $null) -AND ($RemoveLogPath -ne ""))
	{
    echo "******************************************************************"
    Get-ChildItem –Path  "$RemoveLogPath" –Recurse -Exclude "$excludeFiles"
    echo "******************************************************************"
    echo ""
    echo ""
	}
	else
	{
		throw "Log Path Should not be empty or null"
		exit 1
	}

    #Display Old files and store remove file list in txt file
    echo "Display older than [$OldFilesPeriod] days files in Directory"
    echo "******************************************************************"
    $OldFilesContent=Get-ChildItem –Path  "$RemoveLogPath" -Attributes !Directory –Recurse -Exclude "$excludeFiles" | Where-Object { $_.CreationTime –lt (Get-Date).AddDays($OldFilesPeriod) }
    $OldFilesContent
   
    $StoreRemoveList=$RemoveLogPath+"DeletedFileList_$(get-date -f yyyy-MM-dd-ss).txt"
    $OldFilesContent | Out-File -FilePath "$StoreRemoveList" -Encoding ASCII 
    echo "******************************************************************"
    echo ""
    echo ""
    
   

    #Delete delete Old Files
    echo "Remove File : [$RemoveLogPath] : STARTED - $(get-date -f yyyy/MM/dd/ss)"
    echo "-------------------------------------------------"
    Get-ChildItem –Path  "$RemoveLogPath" -Attributes !Directory –Recurse -Exclude "$excludeFiles" | Where-Object { $_.CreationTime –lt (Get-Date).AddDays($OldFilesPeriod) } | Remove-Item -Verbose -Force 
    echo "-------------------------------------------------"
    echo "Files Deleted"
    echo "Remove File : [$RemoveLogPath] : COMPLETED - $(get-date -f yyyy/MM/dd/ss)"
    echo ""
    echo ""

}
catch
{
  Write-Host "ERROR :: Execution Failed. Please check below log"
  echo ""
  throw $_
  exit 1   
}
