
import axios from 'axios';

const BASE_URL = 'http://localhost:5000/api'; // Replace with deployed backend URL

export const loginUser = async (email, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/login`, { email, password });
    return response.data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
};

export const getWalletBalance = async (email) => {
  try {
    const response = await axios.get(`${BASE_URL}/wallet`, { params: { email } });
    return response.data;
  } catch (error) {
    console.error('Wallet fetch error:', error);
    throw error;
  }
};

export const spinSlotMachine = async (email, betAmount) => {
  try {
    const response = await axios.post(`${BASE_URL}/slot`, { email, bet_amount: betAmount });
    return response.data;
  } catch (error) {
    console.error('Slot spin error:', error);
    throw error;
  }
};
