import streamlit as st

def adventure_game():
    st.title("🏰 The Enchanted Castle Adventure")
    
    st.markdown("""
    You find yourself standing before an ancient castle, its gates slightly open.
    You must decide how to proceed.
    """)
    
    choice1 = st.radio("What do you do?", ["Enter through the main gate", "Sneak in through a side window"])
    
    if choice1 == "Enter through the main gate":
        st.write("As you step inside, torches light up along the walls. A long hallway stretches ahead, but a hidden door catches your eye. Do you continue down the hallway or open the secret door?")
        choice2 = st.radio("Your choice:", ["Continue down the hallway", "Open the secret door"])
        
        if choice2 == "Continue down the hallway":
            st.error("A trap is triggered, and you fall into a pit! Game Over.")
        else:
            st.success("You discover a hidden treasure room filled with gold. You Win!")
    
    else:
        st.write("You climb through the window and find yourself in a dimly lit chamber. There's a staircase leading up and a dark passageway leading down. Where do you go?")
        choice2 = st.radio("Your choice:", ["Climb up the staircase", "Explore the dark passageway"])
        
        if choice2 == "Climb up the staircase":
            st.success("You reach the castle tower and find a magical artifact. You Win!")
        else:
            st.error("The passageway is a dead end, and the walls start closing in. Game Over.")

if __name__ == "__main__":
    adventure_game()
