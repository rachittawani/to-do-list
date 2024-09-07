/** @type {import('tailwindcss').Config} */
// @ts-ignore
export default {
  content: ["./src/**/*.{html,js,vue,ts}"],
  darkMode: 'class',
  theme: {},
  plugins: [require('daisyui')],
  daisyui: {
    themes: ['light', 'dark'],
  }
}

