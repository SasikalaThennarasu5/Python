/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
  extend: {
    fontFamily: {
      poppins: ['Poppins', 'sans-serif'],
    },
    colors: {
      peach: '#FFE5B4',
      amber: '#FFAB0D',
      lavender: '#E6E6FA',
    },
  },
},

  plugins: [],
}
