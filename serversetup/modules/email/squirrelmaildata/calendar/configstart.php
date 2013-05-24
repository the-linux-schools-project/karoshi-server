<?php

global $cal_admins, $cal_debug, $max_events_per_day_on_month_view_default,
       $calendar_theme, $color, $show_week_numbers_in_month_view_override_default,
       $day_view_start_time_default, $day_view_end_time_default, 
       $show_small_calendar_default, $always_show_full_event_date_and_time,
       $max_displayable_early_morn_late_nite_event_names,
       $day_view_short_time_default, $highlight_threshold_default, 
       $cal_user_can_override_defaults, $small_calendar_size_default,
       $small_calendar_calID_default, $week_start_day_default,
       $small_calendar_header_color_default, $small_calendar_today_color_default,
       $small_calendar_event_italic_style_default, $small_calendar_event_color_default,
       $small_calendar_day_color_default, $small_calendar_separator_default,
       $small_calendar_show_year_default, $small_calendar_show_today_link_default,
       $small_calendar_inherit_day_background_colors_default,
       $external_calendar_clock_skew_default, $day_view_show_hourly_add_buttons_default,
       $month_view_show_event_start_time_default, $month_view_show_daily_add_buttons_default,
       $useDomainInCalID, $allow_small_calendar, $event_click_to_day_view_default,
       $migrateOldCalendarData;







// Can users override default settings?
// Set to 0 (zero) if not, 1 to enable 
// user overrides.  Note that this will
// completely remove the "Calendar Preferences"
// link from the SquirrelMail Options page.
//
$cal_user_can_override_defaults = 1;



// Turn this off (set to zero) if you can guarantee
// that your usernames are all unique.  If your IMAP
// usernames do NOT already include domain name,
// and there is possibility of overlap between personal
// calendars, you'll want to turn this on.
//
$useDomainInCalID = 0;



// What day of the week do weeks start on?
// Valid values are 0 through 6, or the contants
// SU, MO, TU, WE, TH, FR, SA, where SU is 0 and
// SA is 6.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$week_start_day_default = SU;



// Clicking on events on month view or year view
// can go to the event itself or the day view for
// that event's day.
// 
// 0 = go to event view
// 1 = go to day view
// 
$event_click_to_day_view_default = 0;



// Show times on left side of the day view as small
// as possible?  Set to 1 to show the compacted 
// view, 0 (zero) for regular view.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$day_view_short_time_default = 0;



// Show add buttons next to each hour on left 
// side of the day view?  Set to 1 to show these
// 0 (zero) to hide them.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$day_view_show_hourly_add_buttons_default = 1;



// The threshold at which events will be shown
// in a different color (such as red, to notate 
// importance/urgency)
// Possible values are 0 thru 9, or the constants:
//
// SM_CAL_EVENT_PRIORITY_UNKNOWN
// SM_CAL_EVENT_PRIORITY_EMERGENCY
// SM_CAL_EVENT_PRIORITY_URGENT
// SM_CAL_EVENT_PRIORITY_SERIOUS
// SM_CAL_EVENT_PRIORITY_IMPORTANT
// SM_CAL_EVENT_PRIORITY_NORMAL
// SM_CAL_EVENT_PRIORITY_SECONDARY
// SM_CAL_EVENT_PRIORITY_LOW
// SM_CAL_EVENT_PRIORITY_INSIGNIFICANT
// SM_CAL_EVENT_PRIORITY_IGNORE
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$highlight_threshold_default = SM_CAL_EVENT_PRIORITY_URGENT;



// Event times can be shown in a context-sensitive format
// such as "[Today - Apr 25, 2005]".  If this is desirable,
// this setting must be zero.  If you turn this setting
// on, event times will always be shown with the full date
// and time, regardless of context, such as 
// "[Apr 23, 2005 - Apr 25, 2005]"
// 
// 
$always_show_full_event_date_and_time = 0;



// Calendar Theming
//
// A lot of care has been taken to create theming for the
// calendar that works across most SquirrelMail themes.
// Change these with care, and always test by changing your
// SquirrelMail theme a few times, unless you decide to 
// hard-code these values
//
$calendar_theme = array(
    'day_view_title_background'               => $color[0],
    'day_view_time_header'                    => $color[5],
    'day_view_no_event_background_0'          => $color[12],
    'day_view_no_event_background_1'          => $color[4],
    'day_view_event_background_0'             => $color[0],
    'day_view_event_background_1'             => $color[4],

    'month_view_title_background'             => $color[0],
    'month_view_day_header'                   => $color[5],
    'month_view_today_text'                   => $color[1],
    'helper_month_view_today_background'      => $color[2],
    'month_view_holiday_text'                 => $color[1],
    'month_view_event_text_normal'            => $color[8],
    'month_view_event_text_urgent'            => $color[1],
    'month_view_day_background'               => $color[4],
    'month_view_weekend_background'           => $color[5], // or set the same as regular days: $color[4],
    'month_view_holiday_background'           => $color[5],
    'month_view_non_month_day_background'     => $color[0],
    'month_view_non_month_weekend_background' => $color[0],
    'month_view_non_month_holiday_background' => $color[0],
                       );



// The maximum number of events shown for any one
// day in the month view
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$max_events_per_day_on_month_view_default = 4;



// Show event start times on month view?
// Set to 1 to show times, or 0 (zero)
// to hide them.
// 
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$month_view_show_event_start_time_default = 0;



// Show add buttons next to each day on month view?
// Set to 1 to show these 0 (zero) to hide them.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$month_view_show_daily_add_buttons_default = 0;



// The hour of the day to start showing on the day view 
// screen (given based on 24-hour time: 0 - 23)
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$day_view_start_time_default = 7;



// The hour of the day to stop showing on the day view 
// screen (given based on 24-hour time: 0 - 23)
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$day_view_end_time_default = 20;



// The maximum number of event names displayed at the
// bottom of the day view screen for events that fall
// outside the displayable hours specified by 
// $day_view_start_time and $day_view_end_time above
//
$max_displayable_early_morn_late_nite_event_names = 4;



// An extra column can be shown to the left on the month view
// screen with the week number in it if desired.  Set to
// 1 to show week numbers, 0 (zero) to hide them.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$show_week_numbers_in_month_view_override_default = 0;



// Enable small (miniature) calendar?
//
$allow_small_calendar = 1;



// Show the miniature calendar view beneath the
// folder list?  Set to 1 to enable it, or 0 (zero)
// to hide it.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$show_small_calendar_default = 0;



// Text size of miniature calendar view, per CSS
// font-size attribute format.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_size_default = '14px';



// Default ID of the calendar to be shown for 
// the miniature calendar view.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_calID_default = 'personal';



// Default color of miniature calendar
// header text.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_header_color_default = $color[11];



// Default color of miniature calendar
// today text.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_today_color_default = $color[8];



// Default text style for event days on
// miniature calendar view.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_event_italic_style_default = 'italic';



// Default color of miniature calendar
// event text.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_event_color_default = $color[2];



// Default color of miniature calendar
// regular day text.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_day_color_default = $color[8];



// Default miniature calendar separator style.
// 0 for no separator, 1 for a <hr>, or 2 for
// a box around whole calendar.
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_separator_default = 0;



// Show year on top of miniature calendar view?
// 1 = yes, 0 (zero) = no
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_show_year_default = 0;



// Show link for "today" on top of miniature calendar?
// 1 = yes, 0 (zero) = no
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_show_today_link_default = 0;



// Show background colors for days for miniature
// calendar view the same as regular calendar view?
// 1 = yes, 0 (zero) = no
//
// If $cal_user_can_override_defaults is turned
// on, this only serves as a default.
//
$small_calendar_inherit_day_background_colors_default = 0;



// Default skew between clocks on local machine and those
// of any machine serving us an external calendar file
// (used to determine if we need to update our cache of
// such a calendar).  Only used when remote machine
// does not supply file modification time in HTTP headers.
//
// Given in minutes
//
$external_calendar_clock_skew_default = 1;



// You may set this to 1 if you want the plugin to attempt
// to automatically convert users' personal calendars from
// older versions of the calendar plugin (both core
// SquirrelMail calendar as well as Shared Calendars plugins)
// Note that this requires you to make the scripts/convert_cal_to_ical.pl
// file accessible to (executable by) your web server.  Here 
// is a sample setup which allows Apache to execute this 
// file when running as the "apache" group:
//
// # chown root:apache scripts/convert_cal_to_ical.pl
// # chmod 754 scripts/convert_cal_to_ical.pl
//
// -rwxr-xr--  1 root apache 2900 Feb 25 16:51 convert_cal_to_ical.pl*
//
// If you have problems getting apache to execute this,
// turn on $cal_debug below to see more debugging output.
//
$migrateOldCalendarData = 0;



// Turn debugging for calendar module on/off
//
$cal_debug = 0;
// Calendar administrators
//
//
// Specify each administrator and whether or not they 
// should have access to ALL calendars ("yes" or "no")
// (if "no", this administrator can only edit calendars
// that they own)
//
//
// These users can administer the calendars that they
// have created (and optionally ALL calendars) by going
// to Options->Calendar Administration
//
//
// Note that you may use the wildcards * and ? in the
// usernames, where * means "zero or more of any character"
// and ? means "exactly one character"
//
//
$cal_admins = array(

// for example only, real entries
// should not have the two slashes
// at the beginning of the line:
//
//   'martina*'           => 'yes',
//   'pavel@example.net'  => 'yes',
//   'jennifer@example.*' => 'no',

