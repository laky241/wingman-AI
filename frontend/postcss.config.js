/** @type {import('postcss').Config} */
module.exports = {
    plugins: {
      '@tailwindcss/postcss': {}, // ✅ use new plugin instead of 'tailwindcss'
      autoprefixer: {},
    },
  };
  