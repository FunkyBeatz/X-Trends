# Web Frens: 𝕏 Trend Discord Bot

![Web Frens Banner](https://i.imgur.com/i9s3LmJ.png)  
*Track the Hottest Trends with Style – Powered by Web Frens 2025 ©*
 
[![Discord](https://img.shields.io/discord/123456789012345678?label=Discord&color=blue)](https://discord.gg/3WaKmnnq)  

[![Web Frens 2025 ©](https://img.shields.io/badge/Web%20Frens%202025%20©-Yellow-brightgreen)](https://x.com/FunkyxBeatz)

## Description
**Web Frens 𝕏 Trending Keywords Bot** is a state-of-the-art Discord bot crafted under the prestigious “Web Frens” brand to deliver real-time trending keywords from X directly to your server. 
Designed with elegance and precision, this bot features a sleek, professional embed interface, dynamic color schemes based on the time of day, and powerful filtering options. 

Powered by Web Frens 2025 ©, it ensures a seamless, branded experience for tracking the latest trends with style and interactivity, now with premium features available via Whop subscriptions.

---

## Commands and Options
Interact with the Web Frens Trending Keywords Bot using the following slash commands, available in any Discord server where the bot is invited:

### `/trending_keywords`
**Description**: Fetch and display trending keywords with customizable filters for an enhanced user experience.

**Options**:
- `hours_ago` *(required, dropdown)*: Select how far back to look for trends, including:
  - `now` (less than 1 hour ago)
  - `1`–`10` (1 to 10 hours ago)
- `keyword_count` *(required, dropdown)*: Specify the number of trending keywords to display (1–10, default: 10).
- `popularity` *(optional, dropdown)*: Filter trends by popularity (Premium feature):
  - `High`
  - `Medium`
  - `Low`
- `category` *(optional, dropdown)*: Filter trends by category (Premium feature):
  - `Tech`
  - `Entertainment`
  - `News`
  - `General`

**Usage Example**:
This command displays the top 3 trending keywords from the last hour, presented in a clean, professional embed with Web Frens branding. *(Premium users can add filters for popularity and category after subscribing on Whop.)*

| Command              | Description                                      | Options                                           |
|----------------------|--------------------------------------------------|---------------------------------------------------|
| `/trending_keywords` | Fetch and display trending keywords              | hours_ago, keyword_count, popularity and category |


**Interactive Features**:
- Click the “`Refresh Trends`” button to manually update trends. *(cooldown: 5 minutes, 5/hour non-premium, 30/hour premium)*

### `/set_notification_role` *(Admin Only)*
**Description**: Enable or disable notifications for trending keywords by setting up a “Keywords” role (admin only).

**Options**:
- `enable` *(required, dropdown)*:
  - `Yes`: Prompts to create a “Keywords” role, enabling pings for trend updates.
  - `No`: Disables notifications for this server.

**Usage Example**:
This command guides admins to create a “Keywords” role, enable mention permissions, and activate notifications for trend updates in `/trending_keywords`.

| Command                  | Description                                      | Options                        |
|--------------------------|--------------------------------------------------|--------------------------------|
| `/set_notification_role` | Sets up a notification role if wanted to         | Yes, No                        |


### `/change_embeds` *(Admin Only, Premium)*
**Description**: Change embed banners for this server (premium feature, admin only).

**Options**:
- `embed_top` *(optional, text)*: Public URL for the top banner (PNG/JPG).
- `embed_bottom` *(optional, text)*: Public URL for the bottom banner (PNG/JPG).
- `preview` *(optional, dropdown)*:
  - `Yes`: Preview changes before applying (ephemeral).
  - `No`: Apply changes directly (default).

**Usage Example**:
This command (for premium users) updates banners, showing a preview if requested, enhancing server branding.

| Command             | Description                                      | Options                                                                         |
|---------------------|--------------------------------------------------|---------------------------------------------------------------------------------|
| `/change_embeds` e.g embed_top:https://i.imgur.com/custom-top.png`     | Changes the banner embeds (Premium Feature)  | embed_top, embed_bottom, preview |


### `/verify_premium`
**Description**: Verify your Web Frens Premium subscription on Whop to unlock premium features.

**Options**:
- `proof` *(required, text)*: Provide proof of Whop subscription (e.g., receipt ID or transaction hash).

**Usage Example**:
This command verifies your premium status, granting access to premium features for 30 days.

| Command             | Description                                      | Options |
|---------------------|--------------------------------------------------|---------|
| `/verify_premium`   | Provide proof of Whop subscription               |  proof  |


### `/ping`
**Description**: Check the bot’s latency to ensure it’s performing well.

**Usage Example**:
This command returns an ephemeral embed with the bot’s latency in milliseconds, branded with Web Frens styling.

| Command | Description             | Options |
|---------|-------------------------|---------|
| `/ping` | Check the bot’s latency |  /      |


### `/web_frens_help`
**Description**: Access help and information about Web Frens features (private to the user).

**Interactive Features**:
- Buttons: “Features,” “Documentation + Problems,” “Contact.”
- Select “Features” for a dropdown of feature details (e.g., Trending Keywords, Filters, Notifications).
- “Documentation + Problems” shows “COMING SOON” for future documentation.
- “Contact” links to [x.com/WebFrens_](https://x.com/WebFrens_) and future Discord support.

---

## Premium Features
Unlock exclusive features with Web Frens Premium, available via Whop subscriptions starting at $6.99/month:
- Custom static embed banners (`/change_embeds`).
- Priority notifications (30 requests/hour, faster updates).
- Preview mode for visual changes (`preview:true` in `/change_embeds`).
- Ad-free branding (remove “Web Frens 2025 ©” watermark).
- Advanced filters (popularity, category).
- 5% discount code (“WEBFRENS5”) for other Web Frens bots/services.
- X-Exclusive trends (coming soon with Twitter API).

Subscribe on Whop, join our Discord, and follow [x.com/WebFrens_](https://x.com/WebFrens_) and [x.com/FunkyxBeatz](https://x.com/FunkyxBeatz) to verify premium access.

---

## Installation, Contributing, License, and Contact
(See previous README for these sections, or let me know if you want updates.)
































