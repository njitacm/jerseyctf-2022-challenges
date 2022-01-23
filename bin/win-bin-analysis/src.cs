using System.Diagnostics;
int coolfunction(string input)
{
    Process.Start("cmd.exe", "/K tree");
    string output = "AES(CBC)"; //encyrption for key
    return 2345325;
}

Process.Start("cmd.exe", "/K tree");
Console.WriteLine($"You really shouldn't run exe's from people that you dont trust {Environment.UserName}");
Console.WriteLine($"SENDING HKEY_CLASSES_ROOT/.386/PersistentHandler {Environment.NewLine}Date: {DateTime.Now:d} Time: {DateTime.Now:t}");
coolfunction("sample text");
var max = 87;
var counter = -42;
string encKey = "HKEY_CURRENT_USER"; //passowrd for key
string words = "njsctf{look-harder}";
for (int i = 0; i < max; i++)
{
    words = words + counter;
    counter += 3;

}

Console.WriteLine($"{Environment.NewLine} {words} ");

string realKey = "U2FsdGVkX1+/+Gg+TT1OswZb7zJBF954sV9CPYr9yjuECuBh60j/qG3Kw4Hk9/l6fu5ibkYarZWNBByLBuGrYQ=="; //solution for key encrypted

Console.ReadLine();