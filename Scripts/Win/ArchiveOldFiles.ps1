#----------------------- # Find  Old files and Archive it #----------------------- #

$LogPath=$arg [0]

#variable declaration
$OldFilesPeriod="-30"
$SourceDir=$LogPath
$excludeFiles="*.zip"
$OldZipFilesPeriod="-30"
$ZipFileExt="*.zip"

try 
{
    #Display existing files
    echo "Display Current files in Directory : [$SourceDir]"
    echo "******************************************************************"
    Get-ChildItem –Path  "$SourceDir" –Recurse -Exclude "$excludeFiles"
    echo "******************************************************************"
    echo ""
    echo ""

    #Display Old files
    echo "Display older than [$OldFilesPeriod] days files in Directory"
    echo "******************************************************************"
    $OldFilesContent=Get-ChildItem –Path  "$SourceDir" –Recurse -Exclude "$excludeFiles" | Where-Object { $_.CreationTime –lt (Get-Date).AddDays($OldFilesPeriod) }
    $OldFilesContent
    echo "******************************************************************"
    echo ""
    echo ""

    #Archive & delete Old Files
    foreach ($OldFile in $OldFilesContent) 
    {
      $ArchiveFileName=$OldFile.Name
      echo "---------------------------------#Archive File Name : $ArchiveFileName #---------------------------------"
      $SplitFileName=$ArchiveFileName.Split(".")[0]
      $ZipFileName=$SplitFileName+".zip"
      $SourceFilePath=$SourceDir+"\"+$ArchiveFileName
      $DestinationFilePath=$SourceDir+"\"+$ZipFileName
	  
	  echo ""
	  echo "Zip / Compress the file : [$SourceFilePath] : STARTED"
      Compress-Archive -Path "$SourceFilePath" -DestinationPath "$DestinationFilePath" -Force
	  echo "Zip /Compress the file : [$SourceFilePath] : COMPLETED"
      Start-Sleep -Seconds 2
	  
	  echo ""
	  echo "Remove File : [$SourceFilePath] : STARTED"
      Remove-Item -Path "$SourceFilePath" -Recurse -Force
      echo "Remove File : [$SourceFilePath] : COMPLETED"
	  Start-Sleep -Seconds 2
	  echo ""
	  echo ""
    }
    echo ""
    echo ""


    #Remove old Archived zip Files
    $OldZipFiles=Get-ChildItem –Path  "$SourceDir" –Recurse -Include "$ZipFileExt" | Where-Object { $_.CreationTime –lt (Get-Date).AddDays($OldZipFilesPeriod) }
    foreach ($OldzipFile in $OldZipFiles) 
    {
      $ZipFileName=$OldzipFile.Name
      echo "Old Zip File Name : $ZipFileName"
      $OldZipFilePath=$SourceDir+"\"+$ZipFileName
      echo "Remove old zip File : [$OldZipFilePath] : STARTED"
      Remove-Item -Path "$OldZipFilePath" -Recurse -Force
      echo "Remove File : [$OldZipFilePath] : COMPLETED"
      Start-Sleep -Seconds 2 
    }
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
