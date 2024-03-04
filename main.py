import pandas as pd


def find_similar_items(item_id, df=pd.read_csv('/Users/antoinebertin/Documents/jedha/full_stack/projects_full_stack/north_face/df.csv')):
    # Find the cluster of the given item
    item_cluster = df.loc[df['id'] == item_id, 'cluster'].iloc[0]
    
    # Find other items in the same cluster
    similar_items = df[df['cluster'] == item_cluster]['id']
    
    # Exclude the item itself and pick up to 5 similar items
    similar_items = similar_items[similar_items != item_id].head(5)
    
    return list(similar_items)

# User interaction part
if __name__ == "__main__":
    try:
        # Ask the user to enter a product ID
        user_input = input("Enter a product ID to find similar items: ")
        item_id = int(user_input)  # Convert input to integer
        
        # Find and display similar items
        similar_items = find_similar_items(item_id)
        if similar_items:
            print(f"Similar items to product ID {item_id}: {similar_items}")
        else:
            print("No similar items found or the item is the only one in its cluster.")
    except ValueError:
        print("Please enter a valid product ID (integer).")
    except IndexError:
        print("The product ID entered does not exist in the dataset.")
