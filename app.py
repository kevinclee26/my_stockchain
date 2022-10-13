import streamlit as st
from datetime import datetime
import stockchain
# from stockchain import StockChain, Block
import pandas as pd

st.title('StockChain Live')
st.write(datetime.utcnow())

@st.cache(allow_output_mutation=True)
def setup(): 
	genisus_block=stockchain.Block(shares=0, buyer_id=0, seller_id=0)
	new_chain=stockchain.StockChain([genisus_block])
	return new_chain

my_chain=setup()

input_shares=st.slider('Please Enter Shares: ')
input_buyer=st.text_input('Please Enter Buyer ID: ')
input_seller=st.text_input('Please Enter Seller ID: ')

if st.button('Submit'): 
	# st.write(input_shares)
	# st.write(input_buyer)
	# st.write(input_seller)
	prev_hash=my_chain.chain[-1].hash_block()
	new_block=stockchain.Block(shares=input_shares, buyer_id=input_buyer, seller_id=input_seller, prev_hash=prev_hash)
	my_chain.add_block(new_block)
else: 
	st.write('No buttons pushed')

# validate
# selected_block=st.sidebar.selectbox('Please Select Block: ', my_chain.chain)
selected_idx=st.sidebar.selectbox('Please Select Block: ', range(len(my_chain.chain)))
selected_block=my_chain.chain[selected_idx]
if st.sidebar.button('Validate'): 
	st.sidebar.write(selected_block.hash_block())

st.write('\n')
st.write('\n')
st.write('\n')

chain_df=pd.DataFrame(my_chain.chain).astype(str)
st.write(chain_df)