// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://flapia.github.io',
  base: '/personal_website',
  vite: {
    plugins: [tailwindcss()]
  }
});