/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      colors: {
        brand: {
          black: '#111111',
          gray: '#f5f5f7',
          accent: '#2563eb',
          accentHover: '#1d4ed8',
          danger: '#ef4444'
        }
      }
    }
  },
  plugins: [],
}
