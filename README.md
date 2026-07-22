# LogoCraft - AI Logo Generator

LogoCraft is a modern web application designed to help users create unique and professional logos using AI. 

## Features

- **AI Logo Generation**: Generate high-quality logos based on text prompts.
- **Customization**: Fine-tune your designs with various styles and color palettes.
- **History**: Keep track of all your generated designs.
- **Modern UI**: A clean, responsive interface built with React and Tailwind CSS.

## Tech Stack

- **Frontend**: React, TypeScript, Vite, Tailwind CSS, Radix UI, Framer Motion.
- **Backend**: Express, tRPC, Drizzle ORM.
- **Database**: MySQL.

## Getting Started

### Prerequisites

- Node.js (v20 or higher)
- pnpm

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/logocraft.git
   cd logocraft
   ```

2. Install dependencies:
   ```bash
   pnpm install
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```env
   DATABASE_URL=your_mysql_database_url
   APP_ID=your_app_id
   COOKIE_SECRET=your_cookie_secret
   OAUTH_SERVER_URL=your_oauth_server_url
   ```

4. Run the development server:
   ```bash
   pnpm dev
   ```

## License

This project is licensed under the MIT License.
