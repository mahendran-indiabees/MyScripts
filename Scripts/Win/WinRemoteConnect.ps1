#############  User Input #################
$CSVFileLocation="C:\Users\Mahendran\Desktop\test.csv"
$ExecuteScriptPath="C:\Users\Mahendran\Desktop\Archivescript.ps1"
######################################


$ServerUserName="Provide Your User Name"
$CybUrl="your cyberark api url"
$ServerPwd =$(Invoke-RestMethod -Uri $CybUrl  -UseBasicParsing -ContentType 'application/json' -Method GET).Content


##### Credential Block ############
$LoginUser=$ServerUserName
$LoginPwd = ConvertTo-SecureString $ServerPwd -AsPlainText -Force
$LoginCredential = New-Object -TypeName System.Management.Automation.PSCredential  -ArgumentList $LoginUser, $LoginPwd
##### Credential Block ############

$CSVRecords = Import-Csv -Path $CSVFileLocation
foreach($RemoteHostData in  $CSVRecords)
{
	$RemoteHostName=$RemoteHostData.ServerID
	$ArchivePath=$RemoteHostData.ServerLogPath
	echo "---------------------------# Connecting Remote Host : [$RemoteHostName] #---------------------------"
	$RemoteSession = New-PSSession -ComputerName $RemoteHostName -Credential $LoginCredential

	echo "---------------------------# Invoke Script Started : [STARTED] #---------------------------"
	Invoke-Command -Session $RemoteSession -FilePath $ExecuteScriptPath -ArgumentList "$ArchivePath"
	echo "---------------------------# Invoke Script Started : [STARTED] #---------------------------"
}