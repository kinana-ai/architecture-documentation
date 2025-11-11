# Localization

## Overview

Kinana is designed for Arabic-speaking markets (UAE, Egypt, GCC) with comprehensive Arabic language support and Right-to-Left (RTL) interface implementation. The platform supports bilingual operation (Arabic/English) with Arabic as the primary language.

**Primary Language**: Arabic  
**Secondary Language**: English  
**Text Direction**: RTL (Right-to-Left) primary, LTR (Left-to-Right) for English

---

## Arabic Language Support

### Language Strategy

**Arabic-First Design**:

- User interface designed in Arabic first
- Content naturally flows in RTL direction
- Arabic typography and font considerations
- Cultural context and linguistic nuances

**Bilingual Capability**:

- Complete translations for both Arabic and English
- User-selectable language preference
- Seamless switching between languages
- Consistent terminology across languages

### Arabic Typography

#### Font Selection

**Recommended Arabic Fonts**:

- **System Fonts**: Tahoma, Arial, SF Pro (iOS), Roboto (Android)
- **Web Fonts**: Montserrat, Cairo, inter-variable, sans-serif
- **Considerations**:
  - Legibility at small sizes
  - Support for diacritics (tashkeel)
  - Unicode coverage
  - Web font performance

**Font Stack Example**:

```css
font-family: "Montserrat", "Cairo", "inter-variable", sans-serif;
```

#### Text Rendering

**Line Height**:

- Arabic requires more line spacing than Latin scripts
- Minimum 1.5 line-height for body text
- Accommodate diacritical marks above and below baseline

**Letter Spacing**:

- Generally avoid letter-spacing in Arabic (disrupts cursive connections)
- Exception: Headings can use slight letter-spacing

**Font Size**:

- Arabic script may appear smaller than Latin at same size
- Consider slightly larger font size for Arabic (e.g., 16px Arabic vs. 14px English)

**Diacritics (Tashkeel)**:

- Support for fully vocalized Arabic text
- Proper rendering of diacritical marks
- Increased line height when diacritics present

### Text Content Guidelines

**Translation Quality**:

- Human translation required (supported by machine translation for UI)
- Culturally appropriate terminology
- Consistent use of formal vs. informal address
- Proper Arabic grammar and spelling

**Localization, Not Just Translation**:

- Date formats: DD/MM/YYYY (common in UAE/Egypt)
- Number formats: 1234 (Western)
- Currency: AED, EGP with proper symbols
- Time formats: 12-hour vs. 24-hour based on locale
- Measurement units: Metric system

**Cultural Considerations**:

- Educational terminology appropriate for region
- Respectful language for Islamic cultural context
- Avoidance of culturally sensitive content
- Gender-appropriate language when needed

---

## RTL Implementation

### RTL Design Principles

**Mirror Interface**:

- Navigation menus: Right to left
- Icons and buttons: Right-aligned
- Text alignment: Right-aligned by default
- Scroll bars: Right side
- Progress indicators: Right to left

**Do Not Mirror**:

- Media controls (play button points right)
- Logos and brand elements
- Graphs and charts (maintain conventional direction)
- Product images
- Icons with directional meaning (back/forward arrows should still be directional)

### CSS Implementation

#### HTML Direction

```html
<html dir="rtl" lang="ar"></html>
```

#### CSS for RTL

```css
/* Logical properties (preferred - work for both RTL and LTR) */
.element {
  margin-inline-start: 20px; /* Left in LTR, Right in RTL */
  margin-inline-end: 10px; /* Right in LTR, Left in RTL */
  padding-inline: 15px; /* Horizontal padding */
  border-inline-start: 1px solid #ccc;
}

/* Directional properties (when logical properties not sufficient) */
[dir="rtl"] .element {
  float: right;
  text-align: right;
  margin-left: 0;
  margin-right: 20px;
}

[dir="ltr"] .element {
  float: left;
  text-align: left;
  margin-right: 0;
  margin-left: 20px;
}
```

#### Flexbox and Grid

```css
/* Flexbox automatically reverses in RTL */
.container {
  display: flex;
  flex-direction: row; /* Reverses to right-to-left in RTL */
}

/* Grid maintains structure, content flows RTL */
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  direction: rtl; /* Content flows right to left */
}
```

#### Icons and Images

```css
/* Mirror icons that indicate direction */
[dir="rtl"] .icon-arrow-forward {
  transform: scaleX(-1);
}

/* Do not mirror icons without directional meaning */
[dir="rtl"] .icon-search {
  transform: none;
}
```

### Angular RTL Support

**Angular Material CDK (Component Dev Kit)**:

```typescript
import { Directionality } from '@angular/cdk/bidi';

constructor(private dir: Directionality) {
  console.log(this.dir.value);  // 'rtl' or 'ltr'
}
```

**Dynamic Direction Change**:

```typescript
// Service to handle language/direction switching
@Injectable()
export class LocalizationService {
  setLanguage(lang: "ar" | "en") {
    const direction = lang === "ar" ? "rtl" : "ltr";
    document.documentElement.setAttribute("dir", direction);
    document.documentElement.setAttribute("lang", lang);
  }
}
```

**Component-Level RTL Handling**:

```typescript
<div [dir]="currentDirection">
  <app-component></app-component>
</div>
```

## Translation Management

#### Translation Process

**Workflow**:

1. Developer extracts new/updated strings
2. XLIFF files sent to translators
3. Translators provide translations in XLIFF format
4. Translated files integrated into project
5. QA review for linguistic accuracy
6. Build platform with translations

**Translation Tools**:

- **Claude AI** (AI based translation)
- Manual editing (by native speaker)

#### 4. Build Configuration

**Angular i18n configuration** (angular.json):

```json
{
  "projects": {
    "kinana": {
      "i18n": {
        "sourceLocale": "en",
        "locales": {
          "ar": "src/locale/messages.ar.xlf"
        }
      },
      "architect": {
        "build": {
          "configurations": {
            "ar": {
              "localize": ["ar"],
              "baseHref": "/ar/"
            }
          }
        }
      }
    }
  }
}
```

**Build commands**:

```bash
# Build English version
ng build --configuration=production

# Build Arabic version
ng build --configuration=ar
```

### Translation Keys Organization

**Namespacing Strategy**:

```
common.save              # Common UI elements
common.cancel
common.submit

auth.login               # Authentication module
auth.logout
auth.forgotPassword

library.uploadDocument   # Library sub-app
library.searchPlaceholder
library.filterByType

videos.playVideo         # Videos sub-app
videos.pauseVideo
```

**Benefits**:

- Organized translation files
- Easy to find related strings
- Prevents key collisions
- Clear module ownership

### Content Translation

#### User-Generated Content

**Strategy**: Not translated automatically

- Content created by users remains in original language
- Optional: Machine translation hints (not displayed as definitive)
- Content language tagging for filtering

#### Static Content

**Strategy**: Full translation

- Platform UI: All strings translated
- Help documentation: Fully translated
- Legal documents: Professional legal translation
- Marketing content: Adapted for locale

#### Dynamic Content

**Strategy**: Database-driven, multi-language storage

```typescript
// Content model with multi-language support
interface MultilingualContent {
  id: string;
  title_ar: string;
  title_en: string;
  description_ar: string;
  description_en: string;
  content_ar: string;
  content_en: string;
}

// Service to get content in user's language
getLocalizedContent(content: MultilingualContent, lang: string) {
  return {
    title: content[`title_${lang}`],
    description: content[`description_${lang}`],
    content: content[`content_${lang}`]
  };
}
```

### Translation Quality Assurance

**QA Process**:

1. **Linguistic review**:

   - Native speaker review
   - Consistency of terminology
   - Cultural appropriateness

2. **Visual QA**:

   - Test in actual UI
   - Check for layout issues
   - Verify RTL display
   - Test with real content lengths

3. **User testing**:
   - Arabic native speakers test platform
   - Feedback on clarity and naturalness
   - Identify confusing translations

---

## Localization Testing

### RTL Testing Checklist

- ☐ All pages render correctly in RTL
- ☐ Navigation flows right to left
- ☐ Text alignment appropriate
- ☐ Scroll bars on correct side
- ☐ Icons mirrored correctly (or not mirrored when shouldn't be)
- ☐ Buttons and forms right-aligned
- ☐ No text overflow or truncation
- ☐ Tooltips and popovers positioned correctly
- ☐ Modal dialogs centered and RTL-aware

### Translation Testing Checklist

- ☐ All UI strings translated (no English in Arabic version)
- ☐ Placeholder text translated
- ☐ Error messages translated
- ☐ Email templates translated
- ☐ Proper date/time/number formats
- ☐ Currency symbols correct
- ☐ No text too long for UI elements
- ☐ Consistent terminology throughout

### Arabic Typography Testing

- ☐ Font renders correctly across browsers
- ☐ Diacritics display properly
- ☐ Line height adequate for Arabic script
- ☐ No character rendering issues
- ☐ Text legible at various sizes
- ☐ Font fallbacks work correctly

---

## Localization Resources

### Standards & Guidelines

- **Unicode Arabic**: https://www.unicode.org/charts/PDF/U0600.pdf
- **CLDR (Common Locale Data Repository)**: http://cldr.unicode.org/
- **W3C Arabic Layout**: https://www.w3.org/TR/alreq/

### Tools

- **Angular i18n**: https://angular.io/guide/i18n-overview
- **Lokalise**: https://lokalise.com/
- **Crowdin**: https://crowdin.com/
- **Google Translate** (reference only, not for production)

### Fonts

- **Google Fonts Arabic**: https://fonts.google.com/?subset=arabic
- **Montserrat**: Open-source, comprehensive coverage
- **Cairo**: Modern, legible Arabic font

---

## Localization Responsibility

**Ownership**:

- **Product Manager**: Translation budget and vendor management
- **Designers**: RTL-aware design, Arabic typography
- **Senior Developer**: i18n implementation, RTL CSS
- **QA/PM**: Translation testing, RTL QA validation

**Translation Vendors**:

- Professional translation services for legal and official content
- In-house review by native speakers
- Continuous improvement based on user feedback

---

_Last Updated: November 2025_  
_Version: 1.0_  
_Primary Language: Arabic (RTL)_
