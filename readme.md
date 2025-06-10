
# Resume Web App

A customizable, dynamic resume website built with HTML, CSS, and JavaScript. Easily update your personal and professional information in a single JavaScript data file and deploy your resume as a web page using GitHub Pages.

---

## What This Project Does

- **Displays a professional resume:** Renders your name, contact info, skills, work experience, and education in a modern, responsive format.
- **Customization via JavaScript:** All resume content is stored in a single JavaScript file (`data.js`). Change the data to reflect any person’s resume—no need to edit HTML.
- **Easy to deploy:** Host your resume online for free using GitHub Pages.

---

## How to Change or Adjust the Info

1. **Edit Personal Data:**
   - Open `assets/data/data.js`.
   - Update the variables (`personalInfo.fullName`, `personalInfo.jobTitle`, `personalInfo.email`, etc.) with your information.
   - Update the `section` arrays for work experience, education and anything else you consider relevant for the primary section, the `sidebarSkills` with your skills and the `sidebarSections` for anything you want displayed there.

2. **Change the Profile Image:**
   - Replace `assets/images/resume-profile.png` with your own image (keep the same file name or update the `personalInfo.profileImage` variable if you use a different one).

3. **Adjust Skills, Experience, and Education:**
   - Add, remove, or modify items in the corresponding JavaScript arrays in `data.js`.

---

## How Is It Constructed?

- **HTML (`index.html`):** The main template contains placeholder elements with unique IDs. It links to styles and scripts, but does not contain hard-coded personal data.
- **CSS (`assets/css/output.css`):** Provides all visual styling, ensuring your resume looks modern and professional.
- **JavaScript (`assets/data/data.js` + `assets/js/render.js`):**  
  - `data.js` contains all resume data as JavaScript variables and arrays.
  - `render.js` contains all the Javascript code that will be executed and will populate it the ` index.html` file with necessary HTML tags
  - The inline `<script>` tags inside `index.html` imports the data and dynamically populates the HTML placeholders with your information.
- **Assets:** Images and icons are stored in the `assets/images` and `assets/fontawesome` directories.

---

## How to Deploy to GitHub Pages

1. **Push Your Code to GitHub:**
   - Create a repository (e.g., `resume`).
   - Push your project files to the repository.

2. **Enable GitHub Pages:**
   - Go to your repository on GitHub.
   - Click **Settings** > **Pages** (or **Pages** in the sidebar).
   - Under **Source**, choose the branch you want to deploy from (usually `main` or `master`), and select the root (`/`) directory.
   - Click **Save**.

3. **Access Your Resume:**
   - After a few minutes, your resume will be live at `https://<your-username>.github.io/<repository-name>/`.

---

## Customization Tips

- For multiple people or resumes, create different versions of `data.js` and swap as needed.
- To extend the resume, add new fields and update the JavaScript/template as required.
- All styling can be adjusted via `assets/css/output.css`.

---

**Feel free to fork this project and make it your own!**  
For questions, open an issue or contribute a pull request.


