/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}', './**/*.{html.j2, html, js}'],
  theme: {
    extend: {
      colors:{
      },
      backgroundSize:{
      },
      fontFamily:{
      },
      backgroundImage:{
      },
      minWidth:{
      },
      screens:{
        'xs': {'max':'639px'},
        'xm': {'max':'768px'},
        'xg': {'max':'1024px'},
      },
      keyframes: {
      },
      animation:{
      }
    },
  },
  plugins: [
  ],
}
