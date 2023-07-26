<?php
$url = 'https://mass.mako.co.il/ClicksStatistics/entitlementsServicesV2.jsp?et=ngt&lp=/direct/hls/live/2033791/k12dvr/index.m3u8?b-in-range=800-2700&rv=AKAMAI';

$content = file_get_contents($url);
$json = json_decode($content, true);
$link = 'http://mako-streaming.akamaized.net/direct/hls/live/2033791/k12dvr/index.m3u8?'.$json['tickets'][0]['ticket'];

header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: '.$link);
exit();
?>
