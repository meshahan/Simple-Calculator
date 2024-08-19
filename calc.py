import streamlit as st

# Initialize session state for the calculator expression and last button press
if 'expression' not in st.session_state:
    st.session_state.expression = ''
if 'last_button' not in st.session_state:
    st.session_state.last_button = None

# Function to update the expression
def update_expression(value):
    st.session_state.expression += value

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except:
        st.session_state.expression = 'Error'

# Function to remove the last character
def backspace():
    st.session_state.expression = st.session_state.expression[:-1]

# Function to clear the entire screen
def clear_screen():
    st.session_state.expression = ''

# Layout for the calculator
st.title('Calculator by "Ibn Adam"')

# Display the current expression with custom style
st.markdown("""
    <style>
    .display {
        background-color: cyan;
        color: black;
        font-weight: bold;
        height: 60px;
        line-height: 60px;
        font-size: 24px;
        text-align: right;
        border-radius: 5px;
        padding: 0 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the current expression
st.markdown(f'<div class="display">{st.session_state.expression}</div>', unsafe_allow_html=True)

# Define button layout for the main calculator buttons
cols = st.columns(4)

# Calculator buttons arranged with div below mult
button_labels = [
    ('7', 'number'), ('8', 'number'), ('9', 'number'), ('add', 'operation'),
    ('4', 'number'), ('5', 'number'), ('6', 'number'), ('sub', 'operation'),
    ('1', 'number'), ('2', 'number'), ('3', 'number'), ('mult', 'operation'),
    ('0', 'number'), ('.', 'number'), ('=', 'operation'), ('div', 'operation')
]

# Display buttons in a grid
for i, (label, button_type) in enumerate(button_labels):
    with cols[i % 4]:
        if st.button(label):
            # Check if the button pressed is different from the last button pressed
            if st.session_state.last_button != label:
                if button_type == 'operation' and label == '=':
                    evaluate_expression()
                elif button_type == 'operation':
                    update_expression({'add': '+', 'sub': '-', 'mult': '*', 'div': '/'}[label])
                else:
                    update_expression(label)
                
                # Update last button pressed
                st.session_state.last_button = label

# Add Backspace and Clear Screen buttons at the bottom
col1, col2 = st.columns([1, 1])
with col1:
    if st.button('Backspace'):
        backspace()
        st.session_state.last_button = 'Backspace'
with col2:
    if st.button('Clear Screen'):
        clear_screen()
        st.session_state.last_button = 'Clear Screen'

# Style for the buttons and heading
st.markdown("""
<style>
/* Heading Style */
h1 {
    background-color: green;
    color: black;
    text-transform: uppercase;
    font-weight: bold;
    padding: 10px;
}

/* Button Styles */
div.stButton > button {
    width: 100%;
    height: 60px;
    font-size: 20px;
    border-radius: 5px;
    margin: 2px;
}

/* General Button Style */
div.stButton > button {
    color: black; /* Font color */
    font-weight: bold; /* Font weight */
}

/* Operation Button Style */
div.stButton > button:nth-of-type(4n+1), 
div.stButton > button:nth-of-type(4n+2), 
div.stButton > button:nth-of-type(4n+3), 
div.stButton > button:nth-of-type(4n+4) {
    background-color: yellow;
}

/* Clear Button Style */
div.stButton > button:nth-of-type(16) { /* Adjust based on the position */
    background-color: #ffcccc;
}
</style>
""", unsafe_allow_html=True)
