<?php

function sky_curl_get_file_contents( $url ){
	$c = curl_init();
	curl_setopt( $c, CURLOPT_RETURNTRANSFER, 1 );
	curl_setopt( $c, CURLOPT_URL, $url );
	$contents = curl_exec( $c );
	curl_close( $c );
	if( $contents ) :
		return $contents;
	else:
		return false;
	endif;
}
$url = 'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_4/hls_fr4/index.m3u8';

$contents = sky_curl_get_file_contents($url);

header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: '.$contents);
exit();
?>