---
name: tech-svelte-frontend
description: Svelte 5 + TypeScript frontend development with Tailwind CSS
version: 1.0.0
---
<!-- TODO: NEEDS REVIEW! -->
# Svelte 5 + TypeScript Frontend Development

Best practices and standards for building modern web applications with Svelte 5.

## Description

Provides technical expertise for building frontend web applications with Svelte 5, TypeScript, Tailwind CSS, and modern web development practices.

## When to Activate

Activate when:
- Repository contains `.svelte` or `.ts` files in `web/` or `frontend/` directory
- User mentions frontend, web app, or UI development
- Implementing frontend features
- Project uses Svelte framework

## Tech Stack

### Core Technologies
- **Framework**: Svelte 5
- **Language**: TypeScript (always prefer over JavaScript)
- **Build Tool**: Vite 6
- **Styling**: Tailwind CSS 4
- **Components**: Shadcn/ui 3.3+
- **Linting**: ESLint (default rules)

### Key Features
- Svelte 5 runes (`$state`, `$derived`, `$effect`)
- TypeScript for type safety
- Component-based architecture
- Reactive state management
- Utility-first CSS with Tailwind

## Svelte 5 Best Practices

### Runes (New in Svelte 5)

**State Management:**
```typescript
<script lang="ts">
  // Reactive state
  let count = $state(0);

  // Derived state
  let doubled = $derived(count * 2);

  // Effects
  $effect(() => {
    console.log(`Count is now ${count}`);
  });

  function increment() {
    count++;
  }
</script>

<button onclick={increment}>
  Count: {count} (Doubled: {doubled})
</button>
```

**Props:**
```typescript
<script lang="ts">
  interface Props {
    title: string;
    count?: number;
  }

  let { title, count = 0 }: Props = $props();
</script>

<h1>{title}</h1>
<p>Count: {count}</p>
```

### Component Structure

**File naming**: `ComponentName.svelte` (PascalCase)

```svelte
<script lang="ts">
  // Imports
  import { Button } from '$lib/components/ui/button';
  import type { User } from '$lib/types';

  // Props
  interface Props {
    user: User;
    onUpdate?: (user: User) => void;
  }

  let { user, onUpdate }: Props = $props();

  // State
  let isEditing = $state(false);

  // Derived
  let displayName = $derived(
    user.firstName + ' ' + user.lastName
  );

  // Functions
  function handleEdit() {
    isEditing = true;
  }

  function handleSave() {
    onUpdate?.(user);
    isEditing = false;
  }
</script>

<!-- Template -->
<div class="user-card">
  {#if isEditing}
    <input bind:value={user.firstName} />
    <Button onclick={handleSave}>Save</Button>
  {:else}
    <h2>{displayName}</h2>
    <Button onclick={handleEdit}>Edit</Button>
  {/if}
</div>

<!-- Styles (scoped by default) -->
<style>
  .user-card {
    /* Component-specific styles */
  }
</style>
```

### TypeScript Usage

**Always use TypeScript**, never plain JavaScript:

```typescript
// Types
export interface User {
  id: number;
  email: string;
  name: string;
  role: 'admin' | 'user';
}

// API calls with types
async function fetchUser(id: number): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) {
    throw new Error('Failed to fetch user');
  }
  return response.json();
}

// Component with typed props
let { users }: { users: User[] } = $props();
```

## Project Structure

```
web/
├── src/
│   ├── lib/
│   │   ├── components/        # Reusable components
│   │   │   ├── ui/           # Shadcn UI components
│   │   │   └── features/     # Feature-specific components
│   │   ├── stores/           # Global state (if needed)
│   │   ├── utils/            # Utility functions
│   │   └── types/            # TypeScript types
│   ├── routes/               # SvelteKit routes
│   │   ├── +page.svelte
│   │   └── users/
│   │       └── [id]/
│   │           └── +page.svelte
│   ├── app.html              # HTML template
│   └── app.css               # Global styles (Tailwind)
├── static/                   # Static assets
├── tests/                    # Tests
└── vite.config.ts
```

## Styling with Tailwind CSS

### Use Utility Classes

```svelte
<div class="flex items-center gap-4 p-6 bg-white rounded-lg shadow-md">
  <img src={user.avatar} alt="" class="w-12 h-12 rounded-full" />
  <div class="flex-1">
    <h3 class="text-lg font-semibold text-gray-900">{user.name}</h3>
    <p class="text-sm text-gray-600">{user.email}</p>
  </div>
</div>
```

### Tailwind Configuration

```javascript
// tailwind.config.js
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        primary: {...},
        secondary: {...}
      }
    }
  },
  plugins: []
}
```

### Component Styles

Use Tailwind for most styling, scoped `<style>` for component-specific needs:

```svelte
<div class="card">
  <!-- Use Tailwind classes primarily -->
</div>

<style>
  /* Only for styles that can't be done with Tailwind */
  .card {
    animation: slideIn 0.3s ease-out;
  }

  @keyframes slideIn {
    from { transform: translateY(-10px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }
</style>
```

## Shadcn/ui Components

### Installation

```bash
npx shadcn-svelte@latest add button
npx shadcn-svelte@latest add card
```

### Usage

```svelte
<script lang="ts">
  import { Button } from '$lib/components/ui/button';
  import { Card } from '$lib/components/ui/card';

  let count = $state(0);
</script>

<Card.Root>
  <Card.Header>
    <Card.Title>Counter</Card.Title>
  </Card.Header>
  <Card.Content>
    <p>Count: {count}</p>
  </Card.Content>
  <Card.Footer>
    <Button onclick={() => count++}>Increment</Button>
  </Card.Footer>
</Card.Root>
```

## State Management

### Local State (Runes)

For component-local state, use Svelte 5 runes:

```typescript
let user = $state<User | null>(null);
let loading = $state(false);
let error = $state<string | null>(null);

async function loadUser(id: number) {
  loading = true;
  error = null;
  try {
    user = await fetchUser(id);
  } catch (e) {
    error = e.message;
  } finally {
    loading = false;
  }
}
```

### Global State (Stores)

For global state, use Svelte stores:

```typescript
// stores/auth.ts
import { writable } from 'svelte/store';
import type { User } from '$lib/types';

export const currentUser = writable<User | null>(null);

export const authStore = {
  subscribe: currentUser.subscribe,
  login: async (email: string, password: string) => {
    const user = await api.login(email, password);
    currentUser.set(user);
  },
  logout: () => {
    currentUser.set(null);
  }
};
```

Usage:
```svelte
<script lang="ts">
  import { authStore } from '$lib/stores/auth';
</script>

{#if $authStore}
  <p>Welcome, {$authStore.name}</p>
{:else}
  <p>Please log in</p>
{/if}
```

## API Integration

### Fetch with Error Handling

```typescript
interface ApiResponse<T> {
  data?: T;
  error?: string;
}

async function apiCall<T>(
  url: string,
  options?: RequestInit
): Promise<ApiResponse<T>> {
  try {
    const response = await fetch(url, {
      headers: {
        'Content-Type': 'application/json',
        ...options?.headers
      },
      ...options
    });

    if (!response.ok) {
      const error = await response.text();
      return { error };
    }

    const data = await response.json();
    return { data };
  } catch (error) {
    return { error: error.message };
  }
}
```

### Usage in Components

```svelte
<script lang="ts">
  import { onMount } from 'svelte';
  import type { User } from '$lib/types';

  let users = $state<User[]>([]);
  let loading = $state(true);
  let error = $state<string | null>(null);

  onMount(async () => {
    const response = await apiCall<User[]>('/api/users');
    if (response.data) {
      users = response.data;
    } else {
      error = response.error;
    }
    loading = false;
  });
</script>

{#if loading}
  <p>Loading...</p>
{:else if error}
  <p class="text-red-600">{error}</p>
{:else}
  {#each users as user (user.id)}
    <UserCard {user} />
  {/each}
{/if}
```

## Forms and Validation

```svelte
<script lang="ts">
  interface FormData {
    email: string;
    password: string;
  }

  let formData = $state<FormData>({
    email: '',
    password: ''
  });

  let errors = $state<Partial<Record<keyof FormData, string>>>({});

  function validate(): boolean {
    errors = {};

    if (!formData.email) {
      errors.email = 'Email is required';
    } else if (!formData.email.includes('@')) {
      errors.email = 'Email is invalid';
    }

    if (!formData.password) {
      errors.password = 'Password is required';
    } else if (formData.password.length < 8) {
      errors.password = 'Password must be at least 8 characters';
    }

    return Object.keys(errors).length === 0;
  }

  async function handleSubmit(e: SubmitEvent) {
    e.preventDefault();
    if (!validate()) return;

    // Submit form
    await apiCall('/api/login', {
      method: 'POST',
      body: JSON.stringify(formData)
    });
  }
</script>

<form onsubmit={handleSubmit}>
  <div>
    <label for="email">Email</label>
    <input
      id="email"
      type="email"
      bind:value={formData.email}
      class="border rounded px-3 py-2"
    />
    {#if errors.email}
      <p class="text-red-600 text-sm">{errors.email}</p>
    {/if}
  </div>

  <div>
    <label for="password">Password</label>
    <input
      id="password"
      type="password"
      bind:value={formData.password}
      class="border rounded px-3 py-2"
    />
    {#if errors.password}
      <p class="text-red-600 text-sm">{errors.password}</p>
    {/if}
  </div>

  <button type="submit">Submit</button>
</form>
```

## Performance Best Practices

### Keyed Each Blocks

Always use keys in `#each` blocks:

```svelte
{#each items as item (item.id)}
  <Item {item} />
{/each}
```

### Lazy Loading

```svelte
<script lang="ts">
  import { onMount } from 'svelte';

  let HeavyComponent;

  onMount(async () => {
    const module = await import('./HeavyComponent.svelte');
    HeavyComponent = module.default;
  });
</script>

{#if HeavyComponent}
  <svelte:component this={HeavyComponent} />
{/if}
```

### Avoid Unnecessary Re-renders

Use `$derived` for computed values instead of recalculating in template:

```typescript
// Good
let filteredItems = $derived(
  items.filter(item => item.active)
);

// Bad (recalculates on every render)
{#each items.filter(item => item.active) as item}
```

## Testing

### Unit Tests (Vitest)

```typescript
import { render, fireEvent } from '@testing-library/svelte';
import Counter from './Counter.svelte';

test('increments counter', async () => {
  const { getByText } = render(Counter);
  const button = getByText('Increment');

  await fireEvent.click(button);

  expect(getByText('Count: 1')).toBeInTheDocument();
});
```

## Instructions

When this skill is active:

1. **Use Svelte 5 Runes**: `$state`, `$derived`, `$effect`, `$props`
2. **Always TypeScript**: Never use plain JavaScript
3. **Tailwind First**: Use utility classes, scoped styles sparingly
4. **Shadcn Components**: Leverage pre-built accessible components
5. **Type Everything**: Props, state, API responses, functions
6. **Handle Errors**: Always handle loading and error states
7. **Validate Forms**: Client-side validation with clear error messages
8. **Performance**: Use keys, lazy loading, derived state
9. **Fetch Latest Docs**: When in doubt about Svelte 5 features

## Integration with Other Skills

- **product-flow-core**: Provides overall workflow and architecture
- **ui-ux-design**: Translates design mockups into Svelte components
- Works alongside backend skill (tech-java-quarkus)

Focus on frontend implementation - let other skills handle their domains.
