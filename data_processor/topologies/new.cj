(ns termproject
  (:use     [streamparse.specs])
  (:gen-class))

(def termproject [options]
   [
    ;; spout configuration
    {"M-spout" (python-spout-spec
          options
          "spouts.messages.Messages"
          ["message"]
          )
    }
    ;; bolt configuration 1 the mongodb bolt
    {"P-bolt" (python-bolt-spec
          options
          {"M-spout" :shuffle}
          "bolts.parsemessage.ParseMessage"
          ["measure"]
          )
    ;; bolt configuration 1 the mongodb bolt
     "F-bolt" (python-bold-spec
          options
          {"P-bolt" ["measure"]}
          "bolts.flatten.Flatten"
          ["record"]
          )
    }
  ]
)
