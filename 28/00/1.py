import locale
import curses
print(curses.baudrate())
print(curses.beep())
print(curses.can_change_color())
print(curses.cbreak())
color_number = 1000
print(curses.color_content(color_number))
print(curses.color_pair(color_number))
print(curses.curs_set(visibility))
print(curses.def_prog_mode())
print(curses.def_shell_mode())
print(curses.delay_output(ms))
print(curses.doupdate())
print(curses.echo())
print(curses.endwin())
print(curses.erasechar())
print(curses.filter())
print(curses.flash())
print(curses.flushinp())
print(curses.getmouse())
print(curses.getsyx())
print(curses.getwin(file))
print(curses.has_colors())
print(curses.has_ic())
print(curses.has_il())
print(curses.has_key(ch))
print(curses.halfdelay(tenths))
print(curses.init_color(color_number, r, g, b))
print(curses.init_pair(pair_number, fg, bg))
print(curses.initscr())
print(curses.is_term_resized(nlines, ncols))
print(curses.isendwin())
print(curses.keyname(k))
print(curses.killchar())
print(curses.longname())
print(curses.meta(flag))
print(curses.mouseinterval(interval))
print(curses.mousemask(mousemask))
print(curses.napms(ms))
print(curses.newpad(nlines, ncols))
print(curses.newwin(nlines, ncols))
print(curses.nl())
print(curses.nocbreak())
print(curses.noecho())
print(curses.nonl())
print(curses.noqiflush())
print(curses.noraw())
print(curses.pair_content(pair_number))
print(curses.pair_number(attr))
print(curses.putp(str))
print(curses.qiflush([flag]))
print(curses.raw())
print(curses.reset_prog_mode())
print(curses.reset_shell_mode())
print(curses.resetty())
print(curses.resize_term(nlines, ncols))
print(curses.resizeterm(nlines, ncols))
print(curses.savetty())
print(curses.setsyx(y, x))
print(curses.setupterm(term=None, fd=-1))
print(curses.start_color())
print(curses.termattrs())
print(curses.termname())
print(curses.tigetflag(capname))
print(curses.tigetnum(capname))
print(curses.tigetstr(capname))
print(curses.tparm(curses.tigetstr('cup'), 5, 3))
print(curses.typeahead(fd))
print(curses.unctrl(ch))
print(curses.ungetch(ch))
print(curses.update_lines_cols())
print(curses.unget_wch(ch))
print(curses.ungetmouse(id, x, y, z, bstate))
print(curses.use_env(flag))
print(curses.use_default_colors())
print(curses.wrapper(func, ...))
