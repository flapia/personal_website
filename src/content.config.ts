import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const papersCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/papers" }),
  schema: z.object({
    title: z.string(),
    year: z.number(),
    journal: z.string(),
    type: z.string(),
    doi: z.string().optional(),
    authors: z.array(z.string()),
    url_pdf: z.string().optional(),
    url_code: z.string().optional(),
    lang: z.enum(['en', 'es']).default('en'),
  })
});

const projectsCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/projects" }),
  schema: z.object({
    title: z.string(),
    category: z.enum(['Academic', 'Industry']),
    role: z.string().optional(),
    year: z.string(),
    location: z.string(),
    description: z.string().optional(),
    description_es: z.string().optional(),
    lang: z.enum(['en', 'es']).default('en'),
  })
});

const teachingCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/teaching" }),
  schema: z.object({
    title: z.string(),
    institution: z.string(),
    role: z.string(),
    year: z.string(),
    category: z.enum(['Course', 'Mentorship']),
    link: z.string().optional(),
    lang: z.enum(['en', 'es']).default('en'),
  })
});

const toolsCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/tools" }),
  schema: z.object({
    title: z.string(),
    title_es: z.string().optional(),
    description: z.string(),
    description_es: z.string().optional(),
    tech: z.array(z.string()),
    githubUrl: z.string().optional(),
    colabUrl: z.string().optional(),
  })
});

export const collections = {
  'papers': papersCollection,
  'projects': projectsCollection,
  'teaching': teachingCollection,
  'tools': toolsCollection
};
