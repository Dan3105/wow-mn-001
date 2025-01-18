const { execSync } = require('child_process');

// List of components to install
const components = [
    'avatar',
    'breadcrumb',
    'collapsible',
    'separator',
    'sidebar',
    'dropdown-menu',
    'table',
    'label'
];

console.log('Installing shadcn-ui components...');
// Convert array to comma-separated string
const componentList = components.join(' ');

try {
  console.log('Installing components:', componentList);
  execSync(`npx shadcn@latest add ${componentList}`, { stdio: 'inherit' });
  console.log('Component installation complete!');
} catch (error) {
  console.error('Failed to install components:', error);
}
