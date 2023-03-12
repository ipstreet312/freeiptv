<?php
$url = 'https://mass.mako.co.il/ClicksStatistics/entitlementsServicesV2.jsp?et=ngt&lp=/direct/hls/live/2035325/k12cc/index.m3u8?as=1&rv=AKAMAI';

$content = file_get_contents($url);
$json = json_decode($content, true);
$link = 'https://mako-streaming.akamaized.net/direct/hls/live/2035325/k12cc/index.m3u8?'.$json['tickets'][0]['ticket'];

header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: '.$link);
exit();
?>