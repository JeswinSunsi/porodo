import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

// Products
export const getProducts = async () => {
  const response = await api.get('/products')
  return response.data
}

export const getProduct = async (id) => {
  const response = await api.get(`/products/${id}`)
  return response.data
}

export const getHomeProducts = async () => {
  const response = await api.get('/home/products')
  return response.data
}

export const getHomeTrendingProducts2 = async () => {
  const response = await api.get('/home/trending-products-2')
  return response.data
}

// Cart
export const getCart = async () => {
  const response = await api.get('/cart')
  return response.data
}

// Reviews
export const getReviews = async () => {
  const response = await api.get('/reviews')
  return response.data
}

// Promotions
export const getPromotions = async () => {
  const response = await api.get('/promotions')
  return response.data
}

export default api
