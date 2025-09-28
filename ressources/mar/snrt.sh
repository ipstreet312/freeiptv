#!/bin/bash

# Define arrays for files and their corresponding token URLs
files=("ressources/mar/aloula.m3u8" "ressources/mar/almaghribia.m3u8" "ressources/mar/arryadia.m3u8"  "ressources/mar/arryadiatnt.m3u8" "ressources/mar/assadissa.m3u8" "ressources/mar/athaqafia.m3u8" "ressources/mar/laayoune.m3u8" "ressources/mar/tamazight.m3u8")
urls=("https://cdn.live.easybroadcast.io/abr_corp/73_aloula_w1dqfwm/playlist_dvr.m3u8"
      "https://cdn.live.easybroadcast.io/abr_corp/73_almaghribia_83tz85q/playlist_dvr.m3u8"
      "https://cdn.live.easybroadcast.io/abr_corp/73_arryadia_k2tgcj0/playlist_dvr.m3u8"
      "https://cdn.live.easybroadcast.io/abr_corp/73_arryadia-tnt_zcmwjdc/playlist_dvr.m3u8"
      "https://cdn.live.easybroadcast.io/abr_corp/73_assadissa_7b7u5n1/playlist_dvr.m3u8"
      "https://cdn.live.easybroadcast.io/abr_corp/73_arrabia_hthcj4p/playlist_dvr.m3u8"
      "https://cdn.live.easybroadcast.io/abr_corp/73_laayoune_pgagr52/playlist_dvr.m3u8"
      "https://cdn.live.easybroadcast.io/abr_corp/73_tamazight_tccybxt/playlist_dvr.m3u8")

# Set headers
referer="https://snrt.player.easybroadcast.io/"
origin="https://snrt.player.easybroadcast.io"
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"

# Loop through both arrays using index tracking
for i in "${!files[@]}"; do
    token_url="https://token.easybroadcast.io/all?url=${urls[$i]}"
    echo "Fetching token for: ${files[$i]}"
    
    # Get the full tokenized URL with headers
    full_tokenized_url=$(wget -qO- --header="Origin: $origin" --header="Referer: $referer" --header="User-Agent: $user_agent" "$token_url")
    
    if [[ -n "$full_tokenized_url" ]]; then
        echo "Tokenized URL received: $full_tokenized_url"
        
        # Extract the channel ID from the original URL
        channel_id=$(echo "${urls[$i]}" | grep -oP '(?<=abr_corp/)[^/]+')
        echo "Channel ID: $channel_id"
        
        # Create a temporary file for processing
        temp_file=$(mktemp)
        
        # Process each line of the M3U8 file
        while IFS= read -r line; do
            if [[ "$line" =~ ^https:// ]]; then
                # This is a URL line - extract the base URL path
                base_url=$(echo "$line" | cut -d'?' -f1)
                
                # Extract the quality-specific path part (everything after channel_id)
                quality_path=$(echo "$base_url" | grep -oP "(?<=${channel_id}/).*")
                
                if [[ -n "$quality_path" ]]; then
                    # Construct the new base URL with the correct structure
                    new_base_url="https://cdn.live.easybroadcast.io/abr_corp/${channel_id}/${quality_path}"
                    
                    # Extract just the query parameters from the tokenized URL
                    query_params=$(echo "$full_tokenized_url" | cut -d'?' -f2-)
                    
                    # Output the new URL
                    echo "${new_base_url}?${query_params}"
                else
                    echo "$line"
                fi
            else
                # This is not a URL line (headers, etc.) - keep as is
                echo "$line"
            fi
        done < "${files[$i]}" > "$temp_file"
        
        # Replace the original file with the processed one
        mv "$temp_file" "${files[$i]}"
        echo "Successfully updated tokens for ${files[$i]}"
    else
        echo "Failed to fetch token for ${files[$i]}"
    fi
    echo "---"
done

exit 0
