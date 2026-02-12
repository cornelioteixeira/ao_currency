// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';
 
/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AO Currency Pro',
  tagline: 'Biblioteca profissional para Moeda Angolana (Kwanza)',
  favicon: 'img/favicon.ico',

  url: 'https://cornelio-teixeira.github.io',
  baseUrl: '/ao-currency-pro/',

  organizationName: 'cornelio-teixeira',
  projectName: 'ao-currency-pro',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl: 'https://github.com/cornelio-teixeira/ao-currency-pro/tree/main/docs_site/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'AO Currency Pro',
        logo: {
          alt: 'AO Currency Pro Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentação',
          },
          {
            href: 'https://github.com/cornelio-teixeira/ao-currency-pro',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Introdução',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Mais',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/cornelio-teixeira/ao-currency-pro',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Cornelio Teixeira. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['python', 'bash'],
      },
    }),
};

export default config;
