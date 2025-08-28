// Render header and sidebar info
window.addEventListener('DOMContentLoaded', () => {
  personalInfo = data.personalInfo;
  sections = data.sections;
  sidebarSkills = data.sidebarSkills;
  sidebarSections = data.sidebarSections;
  document.getElementById('main_title').textContent = `Resume - ${personalInfo.fullName}`;
  document.getElementById('full_name').textContent = personalInfo.fullName;
  document.getElementById('job_title').textContent = personalInfo.jobTitle;
  document.getElementById('summary').innerHTML = personalInfo.summary.replaceAll('\n', '<br/>');
  document.getElementById('linkedin_display_name').textContent = personalInfo.linkedin.displayName;
  document.getElementById('linkedin_url').href = personalInfo.linkedin.url;
  const webEL = document.getElementById('website_url');
  const githbEL = document.getElementById('github_url');
  const emailEL = document.getElementById('email');
  const phoneEL = document.getElementById('phone');
  const profImgEL = document.getElementById('profile_image');
  const infoMap = [
    {
      prop: "email",
      action: value => {
        emailEL.textContent = value;
        emailEL.href = `mailto:${value}`;
      },
      elseAction: () => document.getElementById('gen_email').innerHTML = ""
    },
    {
      prop: "phone",
      action: value => {
        phoneEL.textContent = personalInfo.phone;
        phoneEL.href = `tel:${personalInfo.phone}`;
      },
      elseAction: () => document.getElementById('gen_phone').innerHTML = ""
    },
    {
      prop: "location",
      action: value => {
        document.getElementById('location').textContent = personalInfo.location;
      },
      elseAction: () => document.getElementById('gen_location').innerHTML = ""
    },
    {
      prop: "github",
      action: value => {
        githbEL.href = `https://github.com/${personalInfo.github.username}`;
        document.getElementById('github_username').textContent = personalInfo.github.username;
      },
      elseAction: () => githbEL.outerHTML = ""
    },
    {
      prop: "profileImage",
      action: value => {
        profImgEL.src = personalInfo.profileImage;
      },
      elseAction: () => profImgEL.outerHTML = ""
    },
    {
      prop: "website",
      action: value => {
        webEL.href = personalInfo.website.url;
        document.getElementById('website_name').textContent = personalInfo.website.name;
      },
      elseAction: () => webEL.outerHTML = ""
    },
  ];

  infoMap.forEach(({ prop, action, elseAction }) => {
    if (personalInfo[prop]) {
      action(personalInfo[prop]);
    } else {
      elseAction();
    }
  });

  // DYNAMIC SECTIONS RENDERING
  const container = document.getElementById('dynamic_sections');
  container.innerHTML = sections.map(section => renderSection(section)).join('');

  const skillssidebar = document.getElementById('sidebar_skills_section')
  skillssidebar.innerHTML = renderSidebarSkills(sidebarSkills);

  const sidebar = document.getElementById('sidebar_sections');
  sidebar.innerHTML = sidebarSections.map(renderSidebarSection).join('');
});

// Section renderer: customize per section type
function renderSection(section) {
  let html = `<section id="${section.id}" class="resume-section py-3">`;
  html += `<h3 class="text-uppercase resume-section-heading mb-4">${section.title}</h3>`;
  if (section.type === "work") {
    html += section.items.map(work => `
          <div class="item mb-3">
            <div class="item-heading row align-items-center mb-2">
              <h4 class="item-title col-12 col-md-6 col-lg-8 mb-2 mb-md-0">${work.position}</h4>
              <p class="item-title col-16 col-md-6 col-lg-8 mb-2 mb-md-0">${work.company}</p>
              <div class="item-meta col-12 col-md-6 col-lg-4 text-muted text-start text-md-end">${work.years}</div>
            </div>
            <div class="item-content">
              <p style="font-size:15px">${work.position_summary.replaceAll('\n', '<br/>')}</p>
              <ul class="resume-list">
                ${work.key_acomplishments.map(key => `<li style="font-size:15px">${key}</li>`).join('')}
              </ul>
            </div>
          </div>
        `).join('');
  } else if (section.type === "education") {
    html += section.items.map(edu => `
          <div class="item">
            <h4 class="item-title col-12 col-md-6 col-lg-8 mb-2 mb-md-0">${edu.title}</h4>
            <div style="font-size:15px" class="resume-degree-org">${edu.college}</div>
            <div style="font-size:15px" class="resume-degree-time">${edu.dates}</div>
          </div>
        `).join('');
  } else if (section.type === "certification") {
    html += `<ul class="resume-list">` +
      section.items.map(cert =>
        `<li>${cert.name} — ${cert.issuer} (${cert.year})</li>`
      ).join('') +
      `</ul>`;
  } else if (section.type === "articles") {
    html += `<ul class="resume-list">` +
      section.items.map(article =>
        `<li><a href="${article.url}" target="_blank">${article.title}</a> (${article.date})</li>`
      ).join('') +
      `</ul>`;
  } else {
    // Fallback: simple list
    html += `<ul class="resume-list">` +
      section.items.map(item =>
        `<li>${typeof item === 'string' ? item : JSON.stringify(item)}</li>`
      ).join('') +
      `</ul>`;
  }
  html += `</section>`;
  return html;
}

function renderSidebarSkills(skillsArray) {
  let html = `<h3 class="text-uppercase resume-section-heading mb-4">Skills</h3>`;
  skillsArray.forEach(group => {
    html += `<h4 class="item-title">${group.subheader}</h4>
          <ul class="list-unstyled resume-skills-list">
            ${group.items.map(item => `<li class="mb-2" style="font-size:14px">${item}</li>`).join('')}
          </ul>`;
  });
  return html;
}

function renderSidebarSection(section) {
  let html = `<section class="skills-section py-3">
        <h3 class="text-uppercase resume-section-heading mb-4">${section.title}</h3>`;
  if (section.type === "languages") {
    html += `<ul class="list-unstyled resume-skills-list">` +
      section.items.map(item =>
        `<li class="mb-2" style="font-size:14px">${item}</li>`
      ).join('') +
      `</ul>`;
  } else {
    // Fallback for other section types
    html += `<ul class="list-unstyled">` +
      section.items.map(item =>
        `<li class="mb-2" style="font-size:14px">${item}</li>`
      ).join('') +
      `</ul>`;
  }
  html += `</section>`;
  return html;
}
