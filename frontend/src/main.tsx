/**
 * Programmer: Julie Tong
 * Filename: main.tsx
 * Description: Entry point for the React application and renders the main App component.
 */

import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
