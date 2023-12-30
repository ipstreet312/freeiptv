<?php

// Function to extract 'src' value from HTML content
function extractSrcFromHtml($html_code) {
    $dom = new DOMDocument();
    @$dom->loadHTML($html_code); // Suppress warnings

    $script_tags = $dom->getElementsByTagName('script');
    $src_value = null;

    foreach ($script_tags as $script) {
        if (strpos($script->nodeValue, 'player.source =') !== false) {
            $src_start = strpos($script->nodeValue, "'https://");
            $src_end = strpos($script->nodeValue, ".m3u8'") + strlen(".m3u8'");
            $src_value = substr($script->nodeValue, $src_start, $src_end - $src_start);
            break;
        }
    }

    return $src_value;
}

// Main function to fetch HTML content and extract 'src' value
function main() {
    // Fetch HTML content from the URL
    $url = 'https://webplayer.sbctv.ch/auftanken/';
    $html_code = file_get_contents($url); // Get HTML content
    
    if ($html_code !== false) {
        $src = extractSrcFromHtml($html_code);
        if ($src !== null) {
            $src = trim($src, "'\"");
            $url2 = $src . "\n";
            $content = file_get_contents($url2);

            header('Connection: keep-alive');
            header('Content-Type: application/x-mpegURL');
            header('Location: ' . $content);
            exit();
        } else {
            echo "No 'player.source =' found in the HTML content.\n";
        }
    } else {
        echo "Failed to fetch HTML content.\n";
    }
}

// Execute main function
main();

?>
