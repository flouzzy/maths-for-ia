import unittest
from rename_files import clean_filename

class TestCleanFilename(unittest.TestCase):
    def test_normal_string(self):
        """Test with a string that has no characters to replace."""
        self.assertEqual(clean_filename("Normal File Name.md"), "Normal File Name.md")

    def test_mojibake_replacements(self):
        """Test with strings containing specific mojibake sequences."""
        self.assertEqual(clean_filename("MathÃ©matiques.md"), "Mathematiques.md")
        self.assertEqual(clean_filename("ModÃ¨les.md"), "Modeles.md")
        self.assertEqual(clean_filename("ForÃªt.md"), "Foret.md")
        self.assertEqual(clean_filename("NoÃ«l.md"), "Noel.md")
        self.assertEqual(clean_filename("LÃ .md"), "La.md")
        self.assertEqual(clean_filename("PÃ¢tes.md"), "Pates.md")
        self.assertEqual(clean_filename("CÃ´te.md"), "Cote.md")
        self.assertEqual(clean_filename("SÃ»r.md"), "Sur.md")
        self.assertEqual(clean_filename("FranÃ§ais.md"), "Francais.md")
        self.assertEqual(clean_filename("NaÃ¯f.md"), "Naif.md")
        self.assertEqual(clean_filename("MaÃ®tre.md"), "Maitre.md")
        # Fallback sequence case
        self.assertEqual(clean_filename("ThÃorÃ¨me.md"), "Theoreme.md")

    def test_latex_replacements(self):
        """Test with strings containing predefined LaTeX macro sequences."""
        self.assertEqual(clean_filename("Space $-mathbb{R}^n$.md"), "Space Rn.md")
        self.assertEqual(clean_filename("Space $-mathcal{L}^p$.md"), "Space Lp.md")
        self.assertEqual(clean_filename("Space $-mathbb{R}$.md"), "Space R.md")

    def test_dollar_and_backslash_removal(self):
        """Test that dollar signs and backslashes are completely removed."""
        self.assertEqual(clean_filename("Cost is $100.md"), "Cost is 100.md")
        self.assertEqual(clean_filename("Path is C:\\temp.md"), "Path is C:temp.md")
        self.assertEqual(clean_filename("Mixed $\\ signs.md"), "Mixed  signs.md")

    def test_mixed_replacements(self):
        """Test a string with multiple types of replacements needed."""
        self.assertEqual(
            clean_filename("MathÃ©matiques in $-mathbb{R}^n$ cost $100\\.md"),
            "Mathematiques in Rn cost 100.md"
        )

if __name__ == '__main__':
    unittest.main()
