# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Development Commands

### Local Development Server
```bash
# Python 3 HTTP server (default)
python -m http.server 8000

# Node.js with live reload
npx live-server

# Node.js http-server
npx http-server -p 8000
```

Visit `http://localhost:8000` after starting any server.

### Package Scripts
```bash
npm start      # Start Python HTTP server on port 8000
npm run serve  # Start Node.js HTTP server on port 8000  
npm run dev    # Start live-server with auto-reload
```

## Project Architecture

This is a **static HTML/CSS/JavaScript portfolio website** with no build process or framework dependencies.

### Core Structure
- **index.html**: Single-page application with semantic sections (#hero, #about, #projects, #skills, #contact)
- **css/styles.css**: All styling including CSS variables, responsive design, animations
- **js/script.js**: Interactive features - smooth scrolling, scroll-based navigation highlighting, form handling, intersection observers

### Key Design Patterns

**CSS Architecture**:
- CSS custom properties (variables) defined in `:root` for theming (colors, transitions, shadows)
- Mobile-first responsive design with media queries at 768px and 480px breakpoints
- BEM-like naming for component classes (e.g., `.hero-content`, `.project-card`, `.skill-item`)

**JavaScript Architecture**:
- Vanilla JavaScript - no frameworks or dependencies
- Event-driven with DOM queries at page load
- Three main feature modules:
  1. Smooth scroll navigation with hash-based routing
  2. Active section highlighting using scroll position detection
  3. Intersection Observer API for scroll-based animations on cards

**Navigation Flow**:
- Fixed header with internal hash links (#about, #projects, etc.)
- Smooth scrolling managed by `scrollIntoView` API in script.js
- Active state tracking by comparing scroll position to section offsets

### Form Handling
Contact form currently shows browser alert on submit (line 52 in script.js). To integrate with a backend:
1. Replace alert() with fetch() or XMLHttpRequest call
2. Update form action and method attributes
3. Consider adding CSRF protection or captcha for production

### Styling System
Color scheme controlled via CSS variables in `:root`:
- `--primary-color: #667eea` (gradient start)
- `--secondary-color: #764ba2` (gradient end)
- Change these to rebrand the entire site

### Animation System
- Hero section uses `fadeInUp` keyframe animation with staggered delays
- Cards use intersection observer for lazy fade-in on scroll
- Hover states use CSS transforms for visual feedback

## Deployment

This is a static site deployable to any CDN or static host:
- GitHub Pages: Push to repo, enable Pages in settings
- Netlify/Vercel: Connect repo or drag-and-drop deployment
- No build step required

## Customization Checklist

When personalizing this template:
1. **index.html**: Update name, subtitle, project cards, skills, social links
2. **css/styles.css**: Modify `:root` variables for color scheme
3. **js/script.js**: Implement real form submission (replace alert on line 52)
4. **images/**: Add profile photo or project screenshots
5. **package.json**: Update author, repository URLs
