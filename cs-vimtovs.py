"""

Copyright 2010 Brad Anderson. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY BRAD ANDERSON ``AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of Brad Anderson.

"""

import sys
from string import Template
import re
from optparse import OptionParser


# Not all fields have been replaced as they should be. I have no idea what some fields
# even mean. I replaced just enough to get C++ looking alright using the wombat
# colorscheme. I even left some hardcoded colors in because I'm just that lazy.
# Changes welcome.
VS_TEMPLATE = \
"""
<UserSettings>
	<ApplicationIdentity version="8.0"/>
	<ToolsOptions>
		<ToolsOptionsCategory name="Environment" RegisteredName="Environment"/>
	</ToolsOptions>
	<Category name="Environment_Group" RegisteredName="Environment_Group">
		<Category name="Environment_FontsAndColors" Category="{1EDA5DD4-927A-43a7-810E-7FD247D0DA1D}" Package="{DA9FB551-C724-11d0-AE1F-00A0C90FFFC3}" RegisteredName="Environment_FontsAndColors" PackageName="Visual Studio Environment Package">
			<PropertyValue name="Version">2</PropertyValue>
			<FontsAndColors Version="2.0">
				<Categories>
					<Category GUID="{5C48B2CB-0366-4FBF-9786-0BB37E945687}" FontName="$Font" FontSize="$FontSize" CharSet="0" FontIsDefault="No">
						<Items>
							<Item Name="Plain Text" Foreground="$Normal_guifg" Background="$Normal_guibg" BoldFont="No"/>
							<Item Name="Selected Text" Foreground="$Visual_guifg" Background="$Visual_guibg" BoldFont="No"/>
							<Item Name="Inactive Selected Text" Foreground="$Visual_guifg" Background="Visual_guibg" BoldFont="No"/>
							<Item Name="Current list location" Foreground="0x00A3DBFF" Background="0x01000007" BoldFont="No"/>
						</Items>
					</Category>
					<Category GUID="{9973EFDF-317D-431C-8BC1-5E88CBFD4F7F}" FontName="$Font" FontSize="$FontSize" CharSet="0" FontIsDefault="No">
						<Items>
							<Item Name="Plain Text" Foreground="$Normal_guifg" Background="$Normal_guibg" BoldFont="No"/>
							<Item Name="Selected Text" Foreground="$Visual_guifg" Background="$Visual_guibg" BoldFont="No"/>
							<Item Name="Inactive Selected Text" Foreground="$Visual_guifg" Background="Visual_guibg" BoldFont="No"/>
							<Item Name="Current list location" Foreground="0x00A3DBFF" Background="0x01000007" BoldFont="No"/>
						</Items>
					</Category>
					<Category GUID="{A27B4E24-A735-4D1D-B8E7-9716E1E3D8E0}" FontName="$Font" FontSize="$FontSize" CharSet="0" FontIsDefault="No">
						<Items>
						    
							<Item Name="Plain Text" Foreground="$Normal_guifg" Background="$Normal_guibg" BoldFont="No"/>
							<Item Name="Indicator Margin" Foreground="0x02000000" Background="$Cursor_guibg" BoldFont="No"/>
							<Item Name="Line Numbers" Foreground="$LineNr_guifg" Background="$LineNr_guibg" BoldFont="No"/>
							<Item Name="Visible White Space" Foreground="0x00808080" Background="0x02000000" BoldFont="No"/>
							<Item Name="Comment" Foreground="$Comment_guifg" Background="$Comment_guibg" BoldFont="No"/>
							<Item Name="Compiler Error" Foreground="000000F0" Background="0x02000000" BoldFont="No"/>
							<Item Name="CSS Comment" Foreground="$Comment_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="CSS Keyword" Foreground="$Keyword_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="CSS Property Name" Foreground="0082E6CA" Background="0x02000000" BoldFont="No"/>
							<Item Name="CSS Property Value" Foreground="00E6DB82" Background="0x02000000" BoldFont="No"/>
							<Item Name="CSS Selector" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="CSS String Value" Foreground="008288E6" Background="0x02000000" BoldFont="No"/>
							<Item Name="HTML Attribute" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="HTML Attribute Value" Foreground="008288E6" Background="0x02000000" BoldFont="No"/>
							<Item Name="HTML Comment" Foreground="$Comment_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="HTML Element Name" Foreground="0082E6CA" Background="0x02000000" BoldFont="No"/>
							<Item Name="HTML Operator" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="Identifier" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="Keyword" Foreground="$Keyword_guifg" Background="$Keyword_guibg" BoldFont="No"/>
							<Item Name="Number" Foreground="$Number_guifg" Background="$Number_guibg" BoldFont="No"/>
							<Item Name="Operator" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="Preprocessor Keyword" Foreground="$PreProc_guifg" Background="$PreProc_guibg" BoldFont="No"/>
							<Item Name="Stale Code" Foreground="0x00808080" Background="0x00C0C0C0" BoldFont="No"/>
							<Item Name="String" Foreground="$String_guifg" Background="$String_guibg" BoldFont="No"/>
							<Item Name="String (C# @ Verbatim)" Foreground="00B4E682" Background="0x02000000" BoldFont="No"/>
							<Item Name="Task List Shortcut" Foreground="0x00FFFFFF" Background="0x02C0C0C0" BoldFont="No"/>
							<Item Name="User Keywords" Foreground="$Keyword_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="User Types" Foreground="00D0C999" Background="0x02000000" BoldFont="No"/>
							<Item Name="Warning" Foreground="000000F0" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Attribute" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Attribute Quotes" Foreground="008288E6" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Attribute Value" Foreground="008288E6" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Comment" Foreground="$Comment_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Delimiter" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Keyword" Foreground="$Keyword_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Markup Extension Class" Foreground="0082E6CA" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Markup Extension Parameter Name" Foreground="00E6DB82" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Markup Extension Parameter Value" Foreground="00D0C999" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Name" Foreground="0082E6CA" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Processing Instruction" Foreground="00B4E682" Background="0x02000000" BoldFont="No"/>
							<Item Name="XAML Text" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>							
							<Item Name="XML Attribute" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Attribute Quotes" Foreground="008288E6" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Attribute Value" Foreground="008288E6" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Comment" Foreground="$Comment_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Delimiter" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Doc Attribute" Foreground="00D0C999" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Doc Comment" Foreground="$Comment_guifg" Background="$Keyword_guibg" BoldFont="No"/>
							<Item Name="XML Doc Tag" Foreground="00D0C999" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Keyword" Foreground="$Keyword_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Name" Foreground="0082E6CA" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Processing Instruction" Foreground="0x0015496C" Background="0x02000000" BoldFont="No"/>
							<Item Name="XML Text" Foreground="$Normal_guifg" Background="0x02000000" BoldFont="No"/>
							<Item Name="XSLT Keyword" Foreground="$Keyword_guifg" Background="0x02000000" BoldFont="No"/>																	
						</Items>
					</Category>
				</Categories>
			</FontsAndColors>
		</Category>
	</Category>
</UserSettings>
"""


class VimColorScheme(object):
    
    def __init__(self, cs_file):
        self.groups = {}
        hi_lines = re.findall("^.*hi[ \r\t\v\f]+(\w+)[ \r\t\v\f]+(.+)$", cs_file.read(), re.M)
        for group, options in hi_lines:
            self.groups[group] = {}
            # print group
            for k, v in re.findall("(\w+)\s*=\s*(\S+)", options):
                self.groups[group][k] = v
                # print "  %s=%s" % (k, v)




if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--font", dest="font", help="font face",
                      default="Consolas")
    parser.add_option("-p", "--fontsize", dest="fontsize",
                      help="font point size", default=8)
    parser.add_option("-m", "--vim", dest="vim_colorscheme",
                      help="vim colorscheme file")
    parser.add_option("-s", "--vs", dest="vs_colorscheme",
                      help="visual studio colorscheme file to output")
    (options, args) = parser.parse_args()

    if not options.vim_colorscheme or not options.vs_colorscheme:
        print "Error: --vim and --vs options is required"
        sys.exit()

    vim_cs = VimColorScheme(open(options.vim_colorscheme))

    vs_template = Template(VS_TEMPLATE)
    subs = { "Font" : options.font, "FontSize" : options.fontsize }
    for group, attributes in vim_cs.groups.iteritems():
        #print group
        for k, v in attributes.iteritems():
            vs_k = k
            vs_v = v

            # translate to vs naming
            color_match = re.search("#([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})", vs_v, re.I)

            if vs_k.lower() == "gui" and vs_v.lower() == "bold":
                vs_k = "guibold"
                vs_v = "Yes"
            elif color_match:
                vs_v = "00%s%s%s" % (color_match.group(3), color_match.group(2), color_match.group(1))
            elif vs_v.lower() == "none" and k == "guifg" or k == "guibg":
                vs_v = "0x02000000"
            else:
                continue

            subs["%s_%s" % (group, vs_k)] = vs_v
            #print "  %s_%s = %s" % (group, vs_k, vs_v)

    vs_colorscheme = vs_template.safe_substitute(subs)
    vs_colorscheme = re.sub('\$\w+?_gui[fb]g', "0x02000000", vs_colorscheme)
    vs_colorscheme = re.sub('\$\w+?_guibold', "No", vs_colorscheme)
    open(options.vs_colorscheme, "w").write(vs_colorscheme)

