import webbrowser
import sys
import time
from urls import URL_COLLECTIONS

def website_search(url):
    """
    Opens the specified URL in the user's default web browser.
    """
    print(f"Attempting to open: {url}")
    try:
        webbrowser.open(url)
        print("Webpage should now be open in your browser.")
    except webbrowser.Error as e:
        print(f"Error opening webpage: {e}")
        print("Please ensure you have a web browser installed and set as default.")

if __name__ == "__main__":
    # Check if a category name was provided as an argument
    if len(sys.argv) > 1:
        chosen_category = sys.argv[1].lower() # Get the first argument and convert to lowercase

        if chosen_category in URL_COLLECTIONS:
            urls_to_open = URL_COLLECTIONS[chosen_category]
            search_term = ""
            print(f"\n--- Opening URLs for category: '{chosen_category}' ({len(urls_to_open)} pages) ---")

            if len(sys.argv) > 2:
                search_term = sys.argv[2].replace(" ", "+")
                print(f"Appending search term '{sys.argv[2]}' to each URL.")

            print(f"\n--- Opening URLs for category: '{chosen_category}' ({len(urls_to_open)} pages) ---")

            for url in urls_to_open:
                final_url = (f"{url}{search_term}")
                website_search(final_url)
                # Optional: Add a small delay between opening URLs to avoid overwhelming the browser
                time.sleep(0.10) # waits for 0.5 seconds (half a second)
                

            print("\n--- All pages for the chosen category have been launched. ---")

        else:
            print(f"Error: Category '{chosen_category}' not found in the URL_COLLECTIONS.")
            print("\nAvailable categories are:")
            for category in URL_COLLECTIONS.keys():
                print(f"- {category}")
            print("\nPlease choose one of the available categories.")
    else:
        print("Usage: python your_script_name.py <category_name>")
        print("\nExample: python open_web_category.py news_sites")
        print("\nAvailable categories:")
        for category in URL_COLLECTIONS.keys():
            print(f"- {category}")


            