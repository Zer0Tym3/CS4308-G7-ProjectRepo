using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS4308_G7_Project_Deliverable1
{

    // sum fuckin bullshit

    class Token
    {
        public Token(String self, int ID)
        {
            this.Self = self;
            this.ID = ID;
        }
        public string Self { get; }
        public int ID { get; }

        private static readonly Dictionary<string, List<Token>> tokenDictionary = new Dictionary<string, List<Token>>
        {
            {"keywords", new List<Token> {
                new Token("import", 0),
                new Token("implementations", 1),
                new Token("function", 2),
                new Token("main", 3),
                new Token("return", 4),
                new Token("type", 5),
                new Token("integer", 6),
                new Token("double", 7),
                new Token("char", 8),
                new Token("num", 9),
                new Token("is", 10)
                //...
            
            } },
            {"identifiers", new List<Token> {
                //...

            } },
            {"operators", new List<Token> {
                //...
            } }
            //...
        };

        
    }
}
