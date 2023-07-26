<?php
$url = 'https://services.iol.pt/matrix?userId=';

$options = array(
  'http'=>array(
    'method'=>"GET",
    'header'=>"User-Agent: User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36&Referer=https://tviplayer.iol.pt"
  )
);
$context = stream_context_create($options);
$response = file_get_contents($url, false, $context);

$link = 'https://video-auth6.iol.pt/live_tvi_internacional/live_tvi_internacional/playlist.m3u8?wmsAuthSign='.$response;

header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: '.$link);
exit();
?>