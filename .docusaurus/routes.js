import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/blog',
    component: ComponentCreator('/blog', 'd18'),
    exact: true
  },
  {
    path: '/blog/archive',
    component: ComponentCreator('/blog/archive', '182'),
    exact: true
  },
  {
    path: '/blog/authors',
    component: ComponentCreator('/blog/authors', '0b7'),
    exact: true
  },
  {
    path: '/blog/authors/all-sebastien-lorber-articles',
    component: ComponentCreator('/blog/authors/all-sebastien-lorber-articles', '4a1'),
    exact: true
  },
  {
    path: '/blog/authors/yangshun',
    component: ComponentCreator('/blog/authors/yangshun', 'a68'),
    exact: true
  },
  {
    path: '/blog/first-blog-post',
    component: ComponentCreator('/blog/first-blog-post', '89a'),
    exact: true
  },
  {
    path: '/blog/long-blog-post',
    component: ComponentCreator('/blog/long-blog-post', '9ad'),
    exact: true
  },
  {
    path: '/blog/math/tuyen_tinh',
    component: ComponentCreator('/blog/math/tuyen_tinh', '76e'),
    exact: true
  },
  {
    path: '/blog/mdx-blog-post',
    component: ComponentCreator('/blog/mdx-blog-post', 'e9f'),
    exact: true
  },
  {
    path: '/blog/physic/core',
    component: ComponentCreator('/blog/physic/core', '044'),
    exact: true
  },
  {
    path: '/blog/physic/docs/essence/PhysiceEssence',
    component: ComponentCreator('/blog/physic/docs/essence/PhysiceEssence', '15b'),
    exact: true
  },
  {
    path: '/blog/physic/read/main',
    component: ComponentCreator('/blog/physic/read/main', '96b'),
    exact: true
  },
  {
    path: '/blog/tags',
    component: ComponentCreator('/blog/tags', '287'),
    exact: true
  },
  {
    path: '/blog/tags/docusaurus',
    component: ComponentCreator('/blog/tags/docusaurus', '704'),
    exact: true
  },
  {
    path: '/blog/tags/facebook',
    component: ComponentCreator('/blog/tags/facebook', '858'),
    exact: true
  },
  {
    path: '/blog/tags/hello',
    component: ComponentCreator('/blog/tags/hello', '299'),
    exact: true
  },
  {
    path: '/blog/tags/hola',
    component: ComponentCreator('/blog/tags/hola', '00d'),
    exact: true
  },
  {
    path: '/blog/welcome',
    component: ComponentCreator('/blog/welcome', 'd2b'),
    exact: true
  },
  {
    path: '/markdown-page',
    component: ComponentCreator('/markdown-page', '3d7'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', 'f57'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '895'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', 'e61'),
            routes: [
              {
                path: '/docs/category/architecture',
                component: ComponentCreator('/docs/category/architecture', '6d1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/category/computer-network',
                component: ComponentCreator('/docs/category/computer-network', 'c95'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/category/graphics',
                component: ComponentCreator('/docs/category/graphics', '01a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/category/layers',
                component: ComponentCreator('/docs/category/layers', '882'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/category/networks',
                component: ComponentCreator('/docs/category/networks', 'a1e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/category/presentation',
                component: ComponentCreator('/docs/category/presentation', 'b73'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/category/tutorial---extras',
                component: ComponentCreator('/docs/category/tutorial---extras', '9ad'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Architecture/',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Architecture/', '3f1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Architecture/cheatsheet_arch',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Architecture/cheatsheet_arch', 'a10'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Architecture/Core',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Architecture/Core', 'af7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Architecture/ISA',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Architecture/ISA', 'a52'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Graphics/',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Graphics/', '4e5'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/', '847'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/Layers/Application',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/Layers/Application', 'b17'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/Layers/Data link',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/Layers/Data link', '927'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/Layers/Networks',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/Layers/Networks', '788'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/Layers/Physical',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/Layers/Physical', 'd12'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/Layers/Presentation/',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/Layers/Presentation/', '596'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/Layers/Presentation/ZTA_AAA',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/Layers/Presentation/ZTA_AAA', '69f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/Layers/Session',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/Layers/Session', '7bc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/Layers/Transport',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/Layers/Transport', '0b1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/OSI models',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/OSI models', '6f0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Computer Fundamentals/Computer Network/pluginNet',
                component: ComponentCreator('/docs/Computer Fundamentals/Computer Network/pluginNet', 'd64'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Development Core/DATA',
                component: ComponentCreator('/docs/Development Core/DATA', '3d4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Development Core/DSA/',
                component: ComponentCreator('/docs/Development Core/DSA/', '94f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Development Core/SEC/CEH',
                component: ComponentCreator('/docs/Development Core/SEC/CEH', '0e0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Development Core/SEC/Information_Security',
                component: ComponentCreator('/docs/Development Core/SEC/Information_Security', '9c7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Development Core/SQL/DBMS',
                component: ComponentCreator('/docs/Development Core/SQL/DBMS', 'c28'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Development Core/SQL/MySql',
                component: ComponentCreator('/docs/Development Core/SQL/MySql', '58d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Development Core/SQL/NoSql',
                component: ComponentCreator('/docs/Development Core/SQL/NoSql', 'f33'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/diagram',
                component: ComponentCreator('/docs/diagram', 'bfc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/function/bt',
                component: ComponentCreator('/docs/function/bt', 'd67'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/function/Tập Giá Trị',
                component: ComponentCreator('/docs/function/Tập Giá Trị', '4a5'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Systems & Innovation/Innovation Techs/Artificial Intelligence/',
                component: ComponentCreator('/docs/Systems & Innovation/Innovation Techs/Artificial Intelligence/', '906'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Systems & Innovation/Systems/Compiler/',
                component: ComponentCreator('/docs/Systems & Innovation/Systems/Compiler/', '09e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Systems & Innovation/Systems/Compiler/CompilerTest',
                component: ComponentCreator('/docs/Systems & Innovation/Systems/Compiler/CompilerTest', '84f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Systems & Innovation/Systems/Interpreter/',
                component: ComponentCreator('/docs/Systems & Innovation/Systems/Interpreter/', 'db6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Systems & Innovation/Systems/Operating Systems/',
                component: ComponentCreator('/docs/Systems & Innovation/Systems/Operating Systems/', '52c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/intro',
                component: ComponentCreator('/docs/Tutorials/intro', '3b2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-basics/computer-network',
                component: ComponentCreator('/docs/Tutorials/tutorial-basics/computer-network', 'e8f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-basics/congratulations',
                component: ComponentCreator('/docs/Tutorials/tutorial-basics/congratulations', 'c60'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-basics/create-a-blog-post',
                component: ComponentCreator('/docs/Tutorials/tutorial-basics/create-a-blog-post', 'fd9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-basics/create-a-document',
                component: ComponentCreator('/docs/Tutorials/tutorial-basics/create-a-document', '4c9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-basics/create-a-page',
                component: ComponentCreator('/docs/Tutorials/tutorial-basics/create-a-page', '9c0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-basics/deploy-your-site',
                component: ComponentCreator('/docs/Tutorials/tutorial-basics/deploy-your-site', '934'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-basics/markdown-features',
                component: ComponentCreator('/docs/Tutorials/tutorial-basics/markdown-features', 'a63'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-extras/manage-docs-versions',
                component: ComponentCreator('/docs/Tutorials/tutorial-extras/manage-docs-versions', 'b82'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Tutorials/tutorial-extras/translate-your-site',
                component: ComponentCreator('/docs/Tutorials/tutorial-extras/translate-your-site', 'd82'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', 'e5f'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
